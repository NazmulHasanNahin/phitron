from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout as django_logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.generics import RetrieveUpdateAPIView
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer, EmployerRegistrationSerializer, EmployerLoginSerializer
from applications.models import Application
from applications.serializers import ApplicationSerializer
from jobs.models import Job
from jobs.serializers import JobSerializer
from dj_rest_auth.views import LoginView as RestAuthLoginView, LogoutView as RestAuthLogoutView
from django.contrib.sessions.models import Session

# Profile Views
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


# Registration and Authentication
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


# Using dj-rest-auth's LoginView for authentication

# from django.contrib.sessions.models import Session
# from dj_rest_auth.views import LoginView as RestAuthLoginView

# class EmployerLoginView(RestAuthLoginView):
#     serializer_class = EmployerLoginSerializer

#     def post(self, request, *args, **kwargs):
#         # Call the parent class's post method
#         response = super().post(request, *args, **kwargs)

#         # Ensure the session is saved and retrieve the session ID
#         session_id = request.session.session_key
#         if not session_id:
#             request.session.save()  # This creates the session if it doesn't exist
#             session_id = request.session.session_key

#         # Alternatively, retrieve the session data from the Session model
#         session = Session.objects.get(session_key=session_id)
#         session_data = session.get_decoded()

#         # Add session ID to the response data
#         response.data['session_id'] = session_id

#         return Response(response.data)




# Using dj-rest-auth's LogoutView for logout
class LogoutView(RestAuthLogoutView):
    def post(self, request, *args, **kwargs):
        django_logout(request)
        return Response({"detail": "Successfully logged out."})


# Dashboard and Applications Views
class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not hasattr(user, 'employerprofile'):
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
        employer_id = request.user.id
        jobs = Job.objects.filter(employer_id=employer_id)
        applications = Application.objects.filter(job__in=jobs)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
