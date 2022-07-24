from rest_framework import serializers
from .models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            "id",
            "name",
            "first_name",
            "last_name",
            "slug",
            "email",
            "bio",
            "is_approved",
            "is_active",
            "class_history",
        )
