# Generated by Django 4.2.6 on 2023-10-27 18:12

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("ceo", "Chief Executive Officer"),
                            ("cfo", "Chief Financial Officer"),
                            ("coo", "Chief Operating Officer"),
                            ("other", "Other"),
                        ],
                        default="ceo",
                        max_length=32,
                    ),
                ),
                ("meta_data", models.JSONField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="KycDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "document",
                    models.FileField(
                        upload_to=common.utils.unique_media_upload,
                        verbose_name="document",
                    ),
                ),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("voter-id", "Voter Id"),
                            ("aadhar-card", "Aadhar Card"),
                            ("other", "Other"),
                        ],
                        default="aadhar-card",
                        max_length=32,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee_kyc_details",
                        to="employees.employeeprofile",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
