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
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



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
    def post(self, request):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            email_subject = "Welcome to WorkWave!"
            email_body = render_to_string("welcome_email.html", {"user": user})
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message": "Registration successful. Check your email for a welcome message."})
        return Response(serializer.errors)
    
class EmployerLoginView(generics.CreateAPIView):
    serializer_class = EmployerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        login(request, user)
        return Response({"detail": "Successfully logged in."})
    
    
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('employer-login')
    
    
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
        
        
class EmployerApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employer = request.user
        jobs = Job.objects.filter(employer=employer)
        applications = Application.objects.filter(job__in=jobs)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)