from django.shortcuts import render
from rest_framework import viewsets
from appointment.models import *
from appointment.serializers import *


# Create your views here.  this is Appointment section 

class AppointmentViewset(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerailizer
    
    