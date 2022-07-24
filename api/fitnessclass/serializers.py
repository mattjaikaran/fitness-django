from rest_framework import serializers
from .models import FitnessClass


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = (
            "id",
            "name",
            "description",
            "capacity",
            "instructor",
            "location",
            "room",
            "length",
            "price",
            "class_time",
        )
