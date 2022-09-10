from rest_framework import viewsets, mixins
from .models import Instructor
from .serializers import InstructorSerializer


class InstructorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Instructor.objects.all()

    def get_queryset(self):
        return Instructor.objects.all()

    def get_serializer_class(self):
        return InstructorSerializer
