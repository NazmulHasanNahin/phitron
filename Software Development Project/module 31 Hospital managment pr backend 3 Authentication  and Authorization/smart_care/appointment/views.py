from django.shortcuts import render
from rest_framework import viewsets
from appointment.models import *
from appointment.serializers import *


# Create your views here.  this is Appointment section

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerailizer

    # custom query kra

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        patient_id = self.request.query_params.get("patient_id")
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

