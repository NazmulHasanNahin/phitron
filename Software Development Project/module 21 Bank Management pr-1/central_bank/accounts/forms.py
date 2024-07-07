from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.constants import *
from accounts.models import *



class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_adress = forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=["username","first_name","last_name","password1","password2","email","gender","birth_date","account_type","city","postal_code","street_adress","country"]
    
    def save(self, commit: True) -> Any:
        our_user= super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type=self.cleaned_data.get("account_type")
            postal_code=self.cleaned_data.get("postal_code")
            gender=self.cleaned_data.get("gender")
            country=self.cleaned_data.get("country")
            birth_date=self.cleaned_data.get("birth_date")
            city=self.cleaned_data.get("city")
            street_adress=self.cleaned_data.get("street_adress")
            
            UserAdress.objects.create(
                user=our_user,
                street_adress=street_adress,
                city=city,
                postal_code=postal_code,
                country=country,
                
            )
            UserBankAccount.objects.create(
                user=our_user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=10000+our_user.id
            )
            
            return our_user
        
        
    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })