from django.db import models
from .base import TimeStampedModel


class Organization(TimeStampedModel):
    owner = models.ForeignKey(
        'api.User',
        on_delete=models.CASCADE,
        related_name='owned_organizations'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)
