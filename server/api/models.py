from django.db import models
from django.contrib.auth.models import AbstractUser

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser, TimeStampedModel):
    age = models.IntegerField(null=True, blank=True)
    organization = models.ForeignKey(
        'Organization', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )


class Organization(TimeStampedModel):
    owner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='owned_organizations'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)