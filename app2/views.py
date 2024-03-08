from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]       #Per View filtering(Locally)
    # filterset_fields = ['city']                   #for  find exact city
    # filterset_fields = ['name','city']            #for  find exact city and name
    # filter_backends = [SearchFilter]
    # search_fields = ['name','city']               #searching for  exact city and name
    # search_fields = ['^name']                     #search = r(first digit of name), start with search
    # search_fields = ['$name']                     # for regex search
    # search_fields = ['@name']                     #for full-text path
    filter_backends = [OrderingFilter]
    # ordering_fields = ['city']
    ordering_fields = ['name''city']








