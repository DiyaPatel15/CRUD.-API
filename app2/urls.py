from django.urls import path, include
from app2 import views


# Creating Router Object


# Register StudentViewSet with Router


urlpatterns = [
    path('studentapi/', views.StudentList.as_view()),

]
