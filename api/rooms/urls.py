from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", DetailRoom.as_view()),
    path("", ListRooms.as_view()),
    path("new", CreateRoom.as_view()),
    path("delete/<int:pk>", DeleteRoom.as_view()),
]
