from django.shortcuts import render
from rest_framework import viewsets
from service.models import *
from service.serializers import *
from rest_framework.routers import DefaultRouter

# Create your views here.  service
class Serviceviewset(viewsets.ModelViewSet):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer