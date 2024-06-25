from django import forms
from profiles.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name', 'about', 'author']

