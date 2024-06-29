from django.shortcuts import render,redirect
from first_app.forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
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
        if rq.method == "POST":
            form=ChangeUserData(rq.POST,instance=rq.user)
            if form.is_valid():
                messages.success(rq,"User Data Changed Succesfully ")
                form.save()
        else:
            form=ChangeUserData(instance=rq.user)
        return render(rq,"profile.html",{"form":form})
    else:
        return redirect("singup")


def user_logout(rq):
    logout(rq)
    return redirect("login")


def pass_change(rq):
    if rq.user.is_authenticated:
        if rq.method == "POST":
            form=PasswordChangeForm(user=rq.user,data=rq.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(rq,form.user)
                return redirect("profile")
        else:
            form=PasswordChangeForm(user=rq.user)
        return render(rq,"pass_change.html",{"form":form})   
    else:
        return redirect("login")

def pass_change_without_old(rq):
    if rq.user.is_authenticated:
        if rq.method == "POST":
            form=SetPasswordForm(user=rq.user,data=rq.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(rq,form.user)
                return redirect("profile")
        else:
            form=SetPasswordForm(user=rq.user)
        return render(rq,"pass_change.html",{"form":form})  
    else:
        return redirect("login") 
            
            

def change_user_data(rq):
    if  rq.user.is_authenticated:
        if rq.method == "POST":
            form=ChangeUserData(rq.POST,instance=rq.user)
            if form.is_valid():
                messages.success(rq,"User Data Changed Succesfully ")
                form.save()
        else:
            form=ChangeUserData()
        return render(rq,"profile.html",{"form":form})
    else:
        return redirect("singup")