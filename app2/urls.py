from django.urls import path, include
from app2 import views


# Creating Router Object


# Register StudentViewSet with Router


urlpatterns = [
    # path('studentapi/', views.StudentList.as_view()),
    path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
]
