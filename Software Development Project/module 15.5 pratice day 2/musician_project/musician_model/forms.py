from django import forms
from musician_model.models import *

class MusicianForm(forms.ModelForm):
    class Meta:
        model=Musician
        fields="__all__"
        