from django.shortcuts import render
from rest_framework import viewsets
from patient.models import *
from patient.serializers import *
from rest_framework.routers import DefaultRouter

# Create your views here.  patient
class Patientviewset(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer