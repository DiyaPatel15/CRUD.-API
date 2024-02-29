from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer

# GENERICAPIVIEW AND MIXINS

# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
# class StudentRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
# class StudentRetrive(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



# In List and Create pk is not required

# class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# # In Retrive and Delete pk is required
#
# class RDUStudent(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)






# CLASS BASED API VIEWS

# class StudentAPI(APIView):
#     def get(self,request,pk=None,format=None):
#         id = pk
#         if id is not None:
#                 stu = Student.objects.get(id=id)
#                 serializer = StudentSerializer(stu)
#                 return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#
#     def post(self, request,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created.'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request,pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated.'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partially Data Updated.'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted.'})


# FUNCTION BASED API VIEWS

# Create your views here.
# @api_view()
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':"Hello World !!"})
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#      print(request.data)
#      return Response({'msg':'This is POST Request.'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == "GET":
#      return Response({'msg': 'This is GET Request.'})
#
#     if request.method == "POST":
#      print(request.data)
#      return Response({'msg':'This is POST Request.','data':request.data})

# FUNCTION BASED API VIEWS

# @api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])  # Bydefault inside this is GET
# def student_api(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         # id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created.'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'PUT':
#         id = pk
#         # id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated.'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'PATCH':
#         id = pk
#         # id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partially Data Updated.'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         id = pk
#         # id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted.'})

