from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", DetailInstructor.as_view()),
    path("", ListInstructors.as_view()),
    path("new", CreateInstructor.as_view()),
    path("delete/<int:pk>", DeleteInstructor.as_view()),
]
