from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField

from common.models import BaseModel

from employees.models import EmployeeProfile
from departments.models import Department


# Create your models here.
User = get_user_model()


class SalaryManagement(BaseModel):
    employee = models.ForeignKey(
        EmployeeProfile, related_name="employee_salaries", on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        Department, related_name="employee_salary_departments", on_delete=models.CASCADE
    )

    is_paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(auto_now=True)
    amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency="SGD", default=0
    )

    """To Do we can add more fields as per requirements"""

    def __str__(self):
        return f"{self.employee}/{self.department}"
