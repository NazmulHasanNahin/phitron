from django.shortcuts import render
from rest_framework import viewsets
from patient.models import *
from patient.serializers import *
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.  patient


class Patientviewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class UserRegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print(user)
            return Response("Done")
        return Response(serializer.errors)
        