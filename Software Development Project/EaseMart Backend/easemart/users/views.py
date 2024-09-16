from django.shortcuts import render
from rest_framework import viewsets
from users.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from .import models
from users.serializers import *


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class UserAcountViewset(viewsets.ModelViewSet):
    queryset = models.UserAccount.objects.all()
    serializer_class =UserAccountSerializer


class UserRegistrationApiView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:7000/users/activate/{uid}/{token}"

            # Send confirmation email
            email_subject = "Confirm Your Email"
            email_body = render_to_string('email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message": "Check your email for confirmation."})

        return Response(serializer.errors)


class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                user_account = UserAccount.objects.get(user=user)

                login(request, user)
                return Response({
                    'token': token.key,
                    'user_id': user_account.id,
                    'account_type': user_account.account_type
                })
            else:
                return Response({'error': "Invalid credentials."})

        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
