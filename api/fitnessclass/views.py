from rest_framework import generics
from .models import FitnessClass
from .serializers import FitnessClassSerializer


class ListFitnessClasses(generics.ListAPIView):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer


class DetailFitnessClass(generics.RetrieveUpdateAPIView):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer


class CreateFitnessClass(generics.CreateAPIView):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer


class DeleteFitnessClass(generics.DestroyAPIView):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer
