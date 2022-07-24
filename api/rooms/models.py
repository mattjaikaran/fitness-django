from django.db import models
from locations.models import Location
import uuid

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, null=True)
    width = models.IntegerField(default=0, max_length=3, null=True)
    length = models.IntegerField(default=0, max_length=3, null=True)
    capacity = models.IntegerField(default=0, max_length=3, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
