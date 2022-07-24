from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", DetailFitnessClass.as_view()),
    path("", ListFitnessClasses.as_view()),
    path("new", CreateFitnessClass.as_view()),
    path("delete/<int:pk>", DeleteFitnessClass.as_view()),
]
