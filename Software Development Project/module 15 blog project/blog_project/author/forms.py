from django import forms
from author.models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = ['name', 'bio', 'phone']

