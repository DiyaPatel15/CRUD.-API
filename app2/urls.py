from django.urls import path, include
from app2 import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
