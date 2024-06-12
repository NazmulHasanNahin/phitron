from django import forms

class contactform(forms.Form):
    name=forms.CharField(label="User Name")
    email=forms.EmailField()
    