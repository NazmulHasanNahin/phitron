from django.shortcuts import render
from rest_framework import viewsets
from contact_us.models import *
from contact_us.serializers import *
from rest_framework.routers import DefaultRouter

# Create your views here.  contact us
class Contactusviewset(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer