from django.apps import AppConfig
from .settings import CUSER_SETTINGS


class coreConfig(AppConfig):
    name = "core"
    verbose_name = CUSER_SETTINGS["app_verbose_name"]
