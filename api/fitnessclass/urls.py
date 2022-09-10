from django.urls import path
from .views import FitnessClassViewSet

urlpatterns = [
    path("classes/", FitnessClassViewSet.as_view()),
]
