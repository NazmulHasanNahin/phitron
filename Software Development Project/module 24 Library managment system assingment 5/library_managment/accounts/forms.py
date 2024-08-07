from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=["username","first_name","last_name" ,"email", "password1", "password2"]
        
        
class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)