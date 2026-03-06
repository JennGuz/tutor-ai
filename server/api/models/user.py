from django.db import models
from django.contrib.auth.models import AbstractUser
from .base import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    age = models.IntegerField(null=True, blank=True)
    organization = models.ForeignKey(
        'api.Organization',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
