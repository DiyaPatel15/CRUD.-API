from django.contrib import admin
from django.urls import path,include



# for direct perform crud in postman in rest framework
from rest_framework.routers import DefaultRouter
from app import views

# router = DefaultRouter()
# router.register('stud', views.StudentViewSet, basename="stud")



urlpatterns = [
     # path('admin/', admin.site.urls),
     # path('studentapp/',views.Student_app),
     path('studentapp/', views.Student_APP.as_view()),

     # path('', include(router.urls))
     # path('stuinfo/<int:pk>', views.student_detail),
     # path('stuinfo/', views.student_list),
]