from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)


# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystu'
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'
#
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystu'



