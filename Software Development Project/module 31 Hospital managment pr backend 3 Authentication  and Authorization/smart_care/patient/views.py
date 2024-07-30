from django.shortcuts import render,redirect
from rest_framework import viewsets
from patient.models import *
from patient.views import *
from django.contrib.auth.models import User
from patient.serializers import *
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# for mail 

from django.core.mail import EmailMultiAlternatives

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
            token=default_token_generator.make_token(user)
            print("token",token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print("uid",uid)
            confirm_link = f"http://127.0.0.1:7000/patient/active/{uid}/{token}"
            email_subject="Confirm Your Email"
            email_body=render_to_string("confirm_email.html",{"confirm_link":confirm_link})
            email=EmailMultiAlternatives(email_subject,"",to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Cheak your mail for confirmation")
        return Response(serializer.errors)
        

def active(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("login")
    else:
        return redirect("register")



class UserLoginAPIView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data["username"]
            password=serializer.validated_data["password"]
            
            user=authenticate(username=username,password=password)
            
            if user:
                token,_=Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({"token":token.key,"user_id":user.id})
            else:
                return Response({"error":"Invalid Crediantial"})
        return Response(serializer.errors)
    
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        logout(request)
        return redirect("login")