from rest_framework import viewsets, mixins
from .models import FitnessClass
from .serializers import FitnessClassSerializer

class FitnessClassViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = FitnessClass.objects.all()

    def get_queryset(self):
        return FitnessClass.objects.all()

    def get_serializer_class(self):
        return FitnessClassSerializer