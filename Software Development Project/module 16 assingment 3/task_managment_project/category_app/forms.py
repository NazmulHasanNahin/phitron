from django import forms
from category_app.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
