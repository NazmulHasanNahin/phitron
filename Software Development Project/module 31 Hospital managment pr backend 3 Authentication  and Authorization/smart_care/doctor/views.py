from django.shortcuts import render
from rest_framework import viewsets,filters,pagination
from doctor.models import *
from doctor.serializers import *
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated

# Create your views here.  doctor

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100

class Doctorviewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class=DoctorPagination


class Specializationviewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class Designationviewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class AvailableTimeforSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset


class AvailableTimeviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends=[AvailableTimeforSpecificDoctor]
    
class Reviewviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
