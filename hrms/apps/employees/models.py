from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from common.models import BaseModel
from common.utils import unique_media_upload

# Create your models here.
User = get_user_model()


class EmployeeProfile(BaseModel):

    """Just added minimum info we have many designation so we can add latter also we can manage dynamic using create model for Designation and add relation here"""

    class Designation(models.TextChoices):
        CEO = "ceo", _("Chief Executive Officer")
        CFO = "cfo", _("Chief Financial Officer")
        COO = "coo", _("Chief Operating Officer")
        OTHER = "other", _("Other")

    user = models.OneToOneField(
        User, related_name="employee_profile", on_delete=models.CASCADE
    )

    designation = models.CharField(
        max_length=32, choices=Designation.choices, default=Designation.CEO
    )

    meta_data = models.JSONField(
        null=True, blank=True
    )  # If we required more info we can use json data

    """To Do we can add more fields as per requirements"""

    def __str__(self):
        return f"{self.user}/{self.designation}"


class KycDetail(BaseModel):

    """Just added minimum info we have many document type so we can add latter also we can manage dynamic using create model for document type"""

    class DocumentType(models.TextChoices):
        VOTER = "voter-id", _("Voter Id")
        AADHAR = "aadhar-card", _("Aadhar Card")
        OTHER = "other", _("Other")

    employee = models.ForeignKey(
        EmployeeProfile, related_name="employee_kyc_details", on_delete=models.CASCADE
    )

    document = models.FileField(_("document"), upload_to=unique_media_upload)

    document_type = models.CharField(
        max_length=32, choices=DocumentType.choices, default=DocumentType.AADHAR
    )
    """To Do we can add more fields as per requirements"""

    def __str__(self):
        return f"{self.employee}/{self.document_type}"
