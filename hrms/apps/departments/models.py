from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from common.models import BaseModel
from common.utils import unique_media_upload
from employees.models import EmployeeProfile

# Create your models here.
User = get_user_model()


class Department(BaseModel):

    """Just added minimum info we have many departments so we can add latter also we can manage dynamic using create model for DepartmentType and add relation here"""

    class DepartmentType(models.TextChoices):
        RECRUITMENT = "recruitment", _("Recruitment")
        PAYROLL = "payroll", _("Payroll")
        OTHER = "other", _("Other")

    employee = models.ForeignKey(
        EmployeeProfile, related_name="employee_departments", on_delete=models.CASCADE
    )
    department_type = models.CharField(
        max_length=32, choices=DepartmentType.choices, default=DepartmentType.PAYROLL
    )

    """To Do we can add more fields as per requirements"""

    def __str__(self):
        return f"{self.employee}/{self.department_type}"
