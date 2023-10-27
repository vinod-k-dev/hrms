from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    PermissionsMixin,
    AbstractBaseUser,
)
from django.contrib.auth.models import Group as BaseGroup
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from common.models import BaseModel


class CUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AbstractCUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

        is_employee = self.is_employee
        is_manager = self.is_manager

        if not self.is_superuser:
            if is_employee and is_manager:
                raise ValidationError(
                    _(
                        "Not acceptable multiple types of user selection, needs to single selection."
                    )
                )

            if not is_employee and not is_manager:
                raise ValidationError(
                    _("Either is_employee or is_manager must be checked.")
                )

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CUser(AbstractCUser, BaseModel):
    """
    Users within the Django core system are represented by this
    model.

    Password and email are required. Other fields are optional.
    """

    is_employee = models.BooleanField(
        _("is_employee"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as employee user. "
        ),
    )

    is_manager = models.BooleanField(
        _("is_manager"),
        default=False,
        help_text=_("Designates whether this user should be treated as manager user. "),
    )

    class Meta(AbstractCUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.email


class Group(BaseGroup):
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
        proxy = True


class Item(BaseModel):
    description = models.TextField()
    quantity = models.IntegerField(_("quantity"), default=0)
    rate = models.DecimalField(_("rate"), max_digits=6, decimal_places=2)

    def __str__(self):
        return "{}".format(self.description)
