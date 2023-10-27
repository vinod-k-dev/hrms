from django.shortcuts import (
    render,
    HttpResponseRedirect,
)

from django.views.generic import (
    ListView,
    CreateView,
)

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from employees.models import EmployeeProfile, KycDetail

from employees.forms import EmployeeKycForm

User = get_user_model()


class KycDetailView(LoginRequiredMixin, CreateView):
    model = KycDetail
    form_class = EmployeeKycForm
    template_name = "employees/emp_kyc_create.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            kyc_obj = form.save(False)
            kyc_obj.employee = request.user.employee_profile
            kyc_obj.save()

            return HttpResponseRedirect(reverse_lazy("employees:kyc_document_list"))

        return render(request, "employees/emp_kyc_create.html", {"form": form})


class KycDetailListView(LoginRequiredMixin, ListView):
    # Here we used SQL query
    queryset = KycDetail.objects.raw("SELECT * FROM employees_kycdetail")
    model = KycDetail
    template_name = "employees/document_list.html"

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.request.user.is_manager:
            """If user is manager then return all documents"""
            return self.queryset
        else:
            """If user is agent then return only our documents"""
            employee_id = self.request.user.employee_profile.id
            # Here we used SQL query
            self.queryset = self.model.objects.raw(
                "SELECT * FROM employees_kycdetail WHERE employee_id = %s",
                [employee_id],
            )
            return self.queryset
