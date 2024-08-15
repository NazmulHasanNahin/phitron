from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.generics import RetrieveUpdateAPIView
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer, EmployerRegistrationSerializer, EmployerLoginSerializer
from applications.models import Application
from applications.serializers import ApplicationSerializer
from jobs.models import Job
from jobs.serializers import JobSerializer


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
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)

    def get(self, request):
        profile = self.get_object()
        serializer = EmployerProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = self.get_object()
        serializer = EmployerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        profile = self.get_object()
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer


class EmployerProfileUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployerProfileSerializer

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)

    def put(self, request):
        profile = self.get_object()
        serializer = EmployerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerRegistrationView(generics.CreateAPIView):
    serializer_class = EmployerRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            email_subject = "Welcome to WorkWave!"
            email_body = render_to_string("welcome_email.html", {"user": user})
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(
                {"message": "Registration successful. Check your email for a welcome message."},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerLoginView(generics.CreateAPIView):
    serializer_class = EmployerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['email'] = user.email
            return Response({"detail": "Successfully logged in."})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        request.session.flush()
        return redirect('employer-login')


class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not hasattr(user, 'employerprofile'):
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

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
