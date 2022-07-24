from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


class ListRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DetailRoom(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoom(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeleteRoom(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
