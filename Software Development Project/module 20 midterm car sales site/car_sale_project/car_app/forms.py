from django import forms
from .models import *

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'title', 'description', 'price', 'image', 'quantity']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
