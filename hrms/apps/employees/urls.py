from django.urls import path, include

from employees.views import *
from rest_framework import routers

from employees.apis import KycDetailViewSet

router = routers.DefaultRouter()
router.register(r"documents", KycDetailViewSet, basename="employee_documents")

app_name = "employees"

urlpatterns = [
    path("create/emp-kyc/", KycDetailView.as_view(), name="create_emp_kyc"),
    path("documents/list/", KycDetailListView.as_view(), name="kyc_document_list"),
    path("", include(router.urls)),
]
