from rest_framework import generics
from .serializers import LocationSerializer
from .models import Location


class ListLocations(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DetailLocation(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CreateLocation(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeleteLocation(generics.DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
