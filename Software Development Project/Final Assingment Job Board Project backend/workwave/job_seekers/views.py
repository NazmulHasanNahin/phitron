from django.http import Http404
from rest_framework import status,viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobSeekerProfile
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from applications.serializers import *
from applications.models import *

class JobSeekerProfileListCreateView(APIView):
    def get(self, request):
        profiles = JobSeekerProfile.objects.all()
        serializer = JobSeekerProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerProfileDetailView(APIView):
    def get_object(self, pk):
        try:
            return JobSeekerProfile.objects.get(pk=pk)
        except JobSeekerProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = JobSeekerProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = JobSeekerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class JobSeekerProfileViewSet(viewsets.ModelViewSet):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    
    
class JobSeekerRegistrationView(generics.CreateAPIView):
    serializer_class = JobSeekerRegistrationSerializer
    
    
class JobSeekerLoginView(generics.CreateAPIView):
    serializer_class = JobSeekerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        login(request, user)
        return Response({"detail": "Successfully logged in."})
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})
    
    
class JobSeekerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        applications = Application.objects.filter(job_seeker=user)  # Ensure 'job_seeker' is the correct field name
        
        applications_data = ApplicationSerializer(applications, many=True).data
        
        return Response({
            'applications': applications_data
        })