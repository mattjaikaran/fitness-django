from django.db import models
import uuid

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=20, unique=True, blank=False)
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
