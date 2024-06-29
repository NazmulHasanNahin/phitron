from django import forms
from catagories.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Catagory
        fields = ['name']