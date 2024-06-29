from django.shortcuts import render,redirect
from first_app.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(rq):
    return render(rq,"home.html")

def singup(rq):
    if not rq.user.is_authenticated:
        if rq.method == "POST":
            form=RegisterForm(rq.POST)
            if form.is_valid():
                messages.success(rq,"ACC Created ")
                form.save()
        else:
            form=RegisterForm()
        return render(rq,"singup.html",{"form":form})
    else:
        return redirect("profile")

def user_login(rq):
    if not rq.user.is_authenticated:
        if rq.method=="POST":
            form=AuthenticationForm(request=rq,data=rq.POST)
            if form.is_valid():
                name=form.cleaned_data["username"]
                userpass = form.cleaned_data["password"]
                user=authenticate(username=name,password=userpass)
                if user is not None:
                    login(rq,user)
                    return redirect("profile")
        else:
            form=AuthenticationForm()
        return render(rq,"login.html",{"form":form})
    else:
        return redirect("profile")
    
def profile(rq):
    if rq.user.is_authenticated:
        return render(rq,"profile.html",{"user":rq.user})
    else:
        return redirect("login")


def user_logout(rq):
    logout(rq)
    return redirect("login")