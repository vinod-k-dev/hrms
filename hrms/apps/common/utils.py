from django.contrib.auth import get_user_model
import logging
import logging.config

from django.utils import timezone

import os
import uuid

User = get_user_model()


def create_logger(handler):
    logger = logging.getLogger(handler)
    return logger


logger = create_logger("app")


def unique_media_upload(instance, filename):
    today = timezone.now().strftime("%Y%m%d")
    name = os.path.basename(filename)
    model_name = instance._meta.verbose_name_raw.replace(" ", "-")

    prefix = uuid.uuid4().hex[:8]

    return f"{model_name}/{instance.id}/{today}/{prefix}-{name}"
