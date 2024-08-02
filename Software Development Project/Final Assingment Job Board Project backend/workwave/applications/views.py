# applications/views.py
from django.http import Http404
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .serializers import ApplicationSerializer

class ApplicationListCreateView(APIView):
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()

            # Send email notification to the job seeker
            user = application.applicant  # Assuming 'applicant' is a ForeignKey to User in your Application model
            email_subject = "Application Submitted Successfully"
            email_body = render_to_string("application_success_email.html", {"user": user, "job": application.job})
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            # Send email notification to the employer
            employer = application.job.employer  # Assuming your Job model has a ForeignKey to Employer
            email_subject = "New Job Application Received"
            email_body = render_to_string("emails/new_application_email.html", {"employer": employer, "application": application})
            email = EmailMultiAlternatives(email_subject, "", to=[employer.user.email])  # Assuming 'user' is the ForeignKey to the Employer's User account
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer