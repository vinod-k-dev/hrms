from django.shortcuts import (
    render,
    HttpResponseRedirect,
    get_object_or_404,
)
from django.contrib.auth import login, authenticate
from django.urls import reverse

from django.views.generic import (
    UpdateView,
    FormView,
    TemplateView,
)

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from core.forms import RegistrationForm, UserProfileForm


from django.contrib.auth import get_user_model

from employees.models import EmployeeProfile


User = get_user_model()


class SignUpView(FormView):
    form_class = RegistrationForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save(False)
        user.set_password(form.cleaned_data.get("password1"))
        user.is_active = True
        user.save()

        user = authenticate(username=user.email, password=form.data["password1"])
        emp_profile = EmployeeProfile.objects.create(user=user)
        login(self.request, user)
        return HttpResponseRedirect(reverse("core:home"))


class ProfileView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        return render(request, "registration/profile.html")


class EditUserProfileView(
    LoginRequiredMixin, UpdateView
):  # Note that we are using UpdateView and not FormView
    model = User
    form_class = UserProfileForm
    template_name = "registration/profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.request.user.pk)

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user

    def get_success_url(self, *args, **kwargs):
        return reverse("core:profile")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "deshboard.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_manager:
            data[
                "employees_count"
            ] = 0  # We can write our code as per our dashboard requirements
        else:
            data["employees_count"] = 0
        return data
