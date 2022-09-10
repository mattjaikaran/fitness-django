from rest_framework import viewsets, mixins
from .serializers import LocationSerializer
from .models import Location

class LocationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Location.objects.all()

    def get_queryset(self):
        return Location.objects.all()

    def get_serializer_class(self):
        return LocationSerializer

