from django.db import models
from locations.models import Location
from rooms.models import Room
from instructors.models import Instructor
import uuid


class FitnessClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, null=True)
    capacity = models.IntegerField(default=0, max_length=3, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    length = models.IntegerField(max_length=2, null=True)
    price = models.IntegerField(max_length=3, null=True)
    class_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
