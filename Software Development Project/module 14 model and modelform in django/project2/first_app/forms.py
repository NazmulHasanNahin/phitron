from django import forms
from first_app.models import *
# from .import models   eta use korte hole models. die name use kora lagbe

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"
        labels={
            "name":"Student Name"
        }
        widgets={
            # "roll":forms.IntegerField()
        }
        help_texts={
            "name":"Write your name here!!"
        }
        error_message={
            "name":{"required":"your name is required"}
        }