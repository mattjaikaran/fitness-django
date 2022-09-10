from django.urls import path
from .views import InstructorViewSet

urlpatterns = [
    path("instructors/", InstructorViewSet.as_view()),
]
