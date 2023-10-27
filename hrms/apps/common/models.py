from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):

    """
    This model defines base models that implements common fields like:
    created_at
    updated_at
    is_deleted
    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        """soft  delete a model instance"""
        if not self.is_deleted:
            self.is_deleted = True
            self.save()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)
