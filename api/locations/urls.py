from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", DetailLocation.as_view()),
    path("", ListLocations.as_view()),
    path("new", CreateLocation.as_view()),
    path("delete/<int:pk>", DeleteLocation.as_view()),
]
