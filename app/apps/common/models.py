from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the project.

    Provides common timestamps and abstract model behavior with a UUID primary key.

    Attributes:
        created_at (models.DateTimeField): Automatically set to the time of model creation.
        updated_at (models.DateTimeField): Automatically updated on every model save.

    Meta:
        abstract (bool): Marks this model as an abstract base class, not intended for direct instantiation.
        get_latest_by (str): Specifies the field to use for ordering when retrieving the latest object.
        ordering (list[str]): Default ordering for all child models, descending by created_at.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at']
