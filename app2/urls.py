from django.urls import path,include
from app2 import views
urlpatterns = [
        # path('studentapp2/', views.hello_world),
        # path('studentapi/', views.student_api),
        # path('studentapi/<int:pk>', views.student_api),
        # path('studentapi/', views.StudentAPI.as_view()),
        # path('studentapi/<int:pk>', views.StudentAPI.as_view()),
        # path('studentapi/', views.LCStudentAPI.as_view()),
        # path('studentapi/', views.StudentCreate.as_view()),
        # path('studentapi/', views.StudentList.as_view()),
        #  path('studentapi/', views.StudentCreate.as_view()),
        # path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),
        # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
        # path('studentapi/<int:pk>', views.StudentDestroy.as_view()),
        # path('studentapi/<int:pk>', views.RDUStudent.as_view()),
        # path('studentapi/', views.StudentListCreate.as_view()),
        # path('studentapi/<int:pk>', views.StudentRetrieveUpdate.as_view()),
        # path('studentapi/<int:pk>', views.StudentRetrieveDestroy.as_view()),
        path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),




]