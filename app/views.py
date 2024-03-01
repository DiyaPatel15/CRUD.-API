from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class Student_APP(View):
 def get(self,request,*args,**kwargs):
     json_data = request.body
     stream = io.BytesIO(json_data)
     print(stream)
     pythondata = JSONParser().parse(stream)
     id = pythondata.get('id', None)
     print(id)
     if id is not None:
         stu = Student.objects.get(id=id)
         serializer = StudentSerializer(stu)
         json_data = JSONRenderer().render(serializer.data)
         return HttpResponse(json_data, content_type='application/json')
     stu = Student.objects.all()
     serializer = StudentSerializer(stu, many=True)
     json_data = JSONRenderer().render(serializer.data)
     return HttpResponse(json_data, content_type='application/json')

 def post(self, request, *args, **kwargs):
     json_data = request.body
     stream = io.BytesIO(json_data)
     print(stream)
     pythondata = JSONParser().parse(stream)
     serializer = StudentSerializer(data=pythondata)
     if serializer.is_valid():
         serializer.save()
         res = {'msg': 'Data Created'}
         json_data = JSONRenderer().render(res)
         return HttpResponse(json_data, content_type='application/json')
     json_data = JSONRenderer().render(serializer.errors)
     return HttpResponse(json_data, content_type='application/json')

 def put(self, request, *args, **kwargs):
     json_data = request.body
     stream = io.BytesIO(json_data)
     print(stream)
     pythondata = JSONParser().parse(stream)
     id = pythondata.get('id')
     stu = Student.objects.get(id=id)
     # comlete update required all data from front end /client
     # serializer = StudentSerializer(stu, data=pythondata,)
     # partially update : all data not required
     serializer = StudentSerializer(stu, data=pythondata, partial=True)
     if serializer.is_valid():
         serializer.save()
         res = {'msg': 'Data Updated !!'}
         json_data = JSONRenderer().render(res)
         return HttpResponse(json_data, content_type='application/json')
     json_data = JSONRenderer().render(serializer.errors)
     return HttpResponse(json_data, content_type='application/json')

 def delete(self, request, *args, **kwargs):
     json_data = request.body
     stream = io.BytesIO(json_data)
     print(stream)
     pythondata = JSONParser().parse(stream)
     id = pythondata.get('id')
     stu = Student.objects.get(id=id)
     stu.delete()
     res = {'msg': 'Data Deleted !!'}
     json_data = JSONRenderer().render(res)
     return HttpResponse(json_data, content_type='application/json')

     # return JsonResponse(res,safe=False)







# @csrf_exempt
# def Student_app(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         print(id)
#         if id is not None:
#           stu = Student.objects.get(id=id)
#           serializer = StudentSerializer(stu)
#           json_data = JSONRenderer().render(serializer.data)
#           return HttpResponse(json_data, content_type='application/json')
#         stu =Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#            serializer.save()
#            res = {'msg':'Data Created'}
#            json_data = JSONRenderer().render(res)
#            return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         # comlete update required all data from front end /client
#         # serializer = StudentSerializer(stu, data=pythondata,)
#         # partially update : all data not required
#         serializer = StudentSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#
#
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data Deleted !!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#
#         # return JsonResponse(res,safe=False)








# for direct perform crud in postman in rest framework
# from rest_framework.viewsets import ModelViewSet
#
#
# # Create your views here.
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# def student_detail(request,pk):
#     stu = Student.objects.get(id=pk)
#     # print(stu)
#     serializer = StudentSerializer(stu)
#     # print(serializer)
#     # print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
#     return HttpResponse(json_data,content_type='application/json')
#
# def student_list(request):
#     stu = Student.objects.all()
#     # print(stu)
#     serializer = StudentSerializer(stu,many=True)
#     # print(serializer)
#     # print(serializer.data)
#     # json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data,safe=False)
#
