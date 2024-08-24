# applications/views.py
from django.http import Http404
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .serializers import ApplicationSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
import logging

# class ApplicationListCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)  # Add this to handle form data

#     def get(self, request):
#         applications = Application.objects.all()
#         serializer = ApplicationSerializer(applications, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         if not request.user.is_authenticated:
#             return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

#         data = request.data.copy()
#         data['job_seeker'] = request.user.id

#         serializer = ApplicationSerializer(data=data)
#         if serializer.is_valid():
#             application = serializer.save()

#             try:
#                 # Send email notification to the employer
#                 employer = application.job.employer
#                 email_subject = "New Job Application Received"
#                 email_body = render_to_string("new_application_email.html", {"employer": employer, "application": application})
#                 email = EmailMultiAlternatives(email_subject, "", to=[employer.email])
#                 email.attach_alternative(email_body, "text/html")
#                 email.send()
                
#                 # Send email notification to the job seeker
#                 job_seeker = application.job_seeker
#                 email_subject = "Application Submitted Successfully"
#                 email_body = render_to_string("application_success_email.html", {"user": job_seeker, "job": application.job})
#                 email = EmailMultiAlternatives(email_subject, "", to=[job_seeker.email])
#                 email.attach_alternative(email_body, "text/html")
#                 email.send()
                
#             except Exception as e:
#                 print(f"Failed to send email: {e}")
#                 return Response({"detail": "Application created but failed to send email notifications."}, status=status.HTTP_201_CREATED)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class ApplicationListCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         serializer = ApplicationSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save(job_seeker=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.views import APIView
# from django.core.mail import send_mail
# from django.conf import settings
# import logging

# from .serializers import ApplicationSerializer

# logger = logging.getLogger(__name__)

# class ApplicationListCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         serializer = ApplicationSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             # Ensure the request user is properly set
#             application = serializer.save(job_seeker=request.user)
#             logger.debug(f"Application created: {application.id}")

#             # Send email notification
#             self.send_email_notifications(application)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             logger.error(f"Application serializer errors: {serializer.errors}")
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def send_email_notifications(self, application):
#         job = application.job
#         job_seeker = application.job_seeker
#         employer_email = job.employer.email

#         subject = f"New Job Application from {job_seeker.username}"
#         message = f"Dear Employer,\n\n{job_seeker.username} has applied for the job '{job.title}' with the cover letter: {application.cover_letter}.\n\nBest regards,\nJob Board Team"
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [employer_email, job_seeker.email]  # Assuming job seeker has an email field

#         try:
#             send_mail(subject, message, from_email, recipient_list)
#             logger.debug(f"Email sent to: {recipient_list}")
#         except Exception as e:
#             logger.error(f"Failed to send email: {e}")



class ApplicationListCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            application = serializer.save(job_seeker=request.user)
            

            # Send email notification to the employer
            try:
                employer = application.job.employer
                email_subject = "New Job Application Received"
                email_body = render_to_string("new_application_email.html", {"employer": employer, "application": application})
                
                email = EmailMultiAlternatives(email_subject, "", to=[employer.email])
                email.attach_alternative(email_body, "text/html")
                email.send()
            except Exception as e:
                print(f"Error sending email to employer: {e}")

            # Send email notification to the job seeker
            try:
                job_seeker = application.job_seeker
                email_subject = "Application Submitted Successfully"
                email_body = render_to_string("application_success_email.html", {"user": job_seeker, "job": application.job})
                email = EmailMultiAlternatives(email_subject, "", to=[job_seeker.email])
                email.attach_alternative(email_body, "text/html")
                email.send()
            except Exception as e:
                print(f"Error sending email to job seeker: {e}")

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