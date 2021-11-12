from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1.api import views

router = DefaultRouter()

router.register('allbooks', views.AllBooks, basename='allbooks')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework'))
]
