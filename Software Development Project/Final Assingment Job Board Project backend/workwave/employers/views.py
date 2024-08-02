# employers/views.py
from rest_framework import status,viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployerProfile
from rest_framework.permissions import IsAuthenticated
from employers.serializers import *
from django.http import Http404
from django.contrib.auth import login,logout
from applications.models import *
from jobs.models import *
from django.http import HttpResponseRedirect
from applications.serializers import *
from jobs.serializers import *
from django.shortcuts import render,redirect




class EmployerProfileListCreateView(APIView):
    def get(self, request):
        profiles = EmployerProfile.objects.all()
        serializer = EmployerProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerProfileDetailView(APIView):
    def get_object(self, pk):
        try:
            return EmployerProfile.objects.get(pk=pk)
        except EmployerProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = EmployerProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = EmployerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    
    
class EmployerRegistrationView(generics.CreateAPIView):
    serializer_class = EmployerRegistrationSerializer
    
    
class EmployerLoginView(generics.CreateAPIView):
    serializer_class = EmployerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        login(request, user)
        return Response({"detail": "Successfully logged in."})
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/employer-login/')

    def get(self, request):
        # Optionally handle GET request for logout
        logout(request)
        return HttpResponseRedirect('/employer-login/')
    
    
class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not hasattr(user, 'employerprofile'):
            return Response({'detail': 'Not authorized'}, status=403)
        
        jobs = Job.objects.filter(employer=user)
        jobs_data = JobSerializer(jobs, many=True).data
        
        applications = Application.objects.filter(job__in=jobs)
        applications_data = ApplicationSerializer(applications, many=True).data
        
        return Response({
            'jobs': jobs_data,
            'applications': applications_data
        })