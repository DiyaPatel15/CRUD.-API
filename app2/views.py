from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]       #Per View filtering(Locally)
    filterset_fields = ['name','city']






