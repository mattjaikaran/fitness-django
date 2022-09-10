from django.urls import path
from .views import LocationViewSet

urlpatterns = [
    path("locations/", LocationViewSet.as_view()),
]
