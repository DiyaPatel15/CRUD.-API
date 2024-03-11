from django.urls import path, include
from app2 import views
from rest_framework.routers import DefaultRouter


# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('singer',views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet,basename='song')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),


]
