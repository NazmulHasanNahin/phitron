from django.shortcuts import render
from rest_framework import viewsets
from doctor.models import *
from doctor.serializers import *
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated

# Create your views here.  doctor


class Doctorviewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class Specializationviewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class Designationviewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class AvailableTimeviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
class Reviewviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
