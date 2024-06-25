from django.shortcuts import render,redirect
from pratice_app.forms import *
# Create your views here.
 
def home(rq):
    if rq.method == "POST":
        form=ExampleForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=ExampleForm()
    return render(rq,"home.html",{"form":form})