from django import forms
from pratice_app.models import *
from .models import ExampleModel, MyModel

class ExampleForm(forms.ModelForm):
    class Meta:
        model=ExampleModel
        fields="__all__"
        
        
        #9# widgets = {
        #     'favorite_color': forms.RadioSelect
        # }