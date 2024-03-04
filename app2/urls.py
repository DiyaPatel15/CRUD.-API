from django.urls import path,include
from app2 import views
urlpatterns = [
        path('studentapi/', views.student_api),
        path('studentapi/<int:pk>', views.student_api),

]