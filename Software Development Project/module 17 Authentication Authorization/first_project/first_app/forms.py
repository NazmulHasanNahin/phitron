from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
    