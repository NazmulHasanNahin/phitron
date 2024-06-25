from django.shortcuts import render,redirect
from profiles.forms import *
# Create your views here.


def add_profile(rq):
    if rq.method == "POST":
        profile_form=ProfileForm(rq.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("add_profile")
        
    else:
        profile_form=ProfileForm()
    return render(rq,"add_profile.html",{"form":profile_form})