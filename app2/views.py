from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from .mypaginations import MyPageNumberPagination
from .mypaginations import MyLimitOffsetPagination



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyPageNumberPagination
    pagination_class = MyLimitOffsetPagination









