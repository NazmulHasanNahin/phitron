from django.shortcuts import render,redirect
from .import models

from first_app.forms import *

# Create your views here.


def home(rq):
    if rq.method == "POST":
        form=StudentForm(rq.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(rq,"home.html",{"form":form})

