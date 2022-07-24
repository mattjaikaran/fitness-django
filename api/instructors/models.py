from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


class Instructor(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    slug = models.CharField(max_length=20, unique=True, blank=False)
    email = models.EmailField(max_length=30, null=False, unique=True)
    bio = models.TextField(max_length=200, null=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    class_history = ArrayField(
        models.CharField(max_length=50, blank=True),
    )

    def __str__(self):
        return self.first_name + self.last_name
