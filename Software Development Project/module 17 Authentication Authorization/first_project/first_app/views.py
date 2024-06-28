from django.shortcuts import render
from first_app.forms import RegisterForm
from django.contrib import messages
# Create your views here.

def home(rq):
    if rq.method == "POST":
        form=RegisterForm(rq.POST)
        if form.is_valid():
            messages.success(rq,"ACC Created ")
            form.save()
    else:
        form=RegisterForm()
    return render(rq,"home.html",{"form":form})