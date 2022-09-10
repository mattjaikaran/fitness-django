from rest_framework import viewsets, mixins
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Room.objects.all()

    def get_queryset(self):
        return Room.objects.all()

    def get_serializer_class(self):
        return RoomSerializer
