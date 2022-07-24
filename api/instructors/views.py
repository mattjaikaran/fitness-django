from rest_framework import generics
from .models import Instructor
from .serializers import InstructorSerializer


class ListInstructors(generics.ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class DetailInstructor(generics.RetrieveUpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CreateInstructor(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class DeleteInstructor(generics.DestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
