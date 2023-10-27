from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from common.models import BaseModel

from employees.models import EmployeeProfile
from common.utils import unique_media_upload

# Create your models here.
User = get_user_model()


class Task(BaseModel):

    """We can add more status as per requirement"""

    class Status(models.TextChoices):
        BACKLOG = "backlog", _("Backlog")
        TODO = "todo", _("To Do")
        INPROGRESS = "in-progress", _("In Progress")
        INREVIEW = "in-review", _("In Review")
        DONE = "done", _("Done")
        OTHER = "other", _("Other")

    employee = models.ForeignKey(
        EmployeeProfile, related_name="employee_tasks", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    eta = models.FloatField(
        default=0,
        help_text="Estimated time for complete the task(Estimated Time of Arrival)",
    )
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    """To Do we can add more fields as per requirements"""

    def __str__(self):
        return f"{self.title}/{self.employee}"


class Attachment(BaseModel):
    task = models.ForeignKey(
        Task, related_name="task_attachments", on_delete=models.CASCADE
    )

    file = models.FileField(_("task_attachments"), upload_to=unique_media_upload)

    def __str__(self):
        return f"{self.task}"
