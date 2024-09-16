from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount,ACCOUNT_TYPE

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserAccountSerializer(serializers.ModelSerializer):
    account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE)

    class Meta:
        model = UserAccount
        fields = ['user', 'mobile_no', 'account_type']

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE,required=True)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'account_type']

    def save(self, **kwargs):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        account_type = self.validated_data['account_type']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Passwords don't match!"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists!"})

        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = False  # For email confirmation
        user.save()

        # Create UserAccount
        UserAccount.objects.create(user=user, account_type=account_type)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)