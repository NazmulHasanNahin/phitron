from django import forms
from musician_model.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model=Musician
        fields="__all__"
        
        
class SingUpForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        