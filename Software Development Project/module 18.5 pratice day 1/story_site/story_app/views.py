from django.shortcuts import render,redirect
from story_app.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.




def singup(rq):
    if rq.method=="POST":
        singup_form=SingUpForm(rq.POST)
        if singup_form.is_valid():
            singup_form.save()
            messages.success(rq,"Your Account have Created Successfully!!!")
            return redirect("login")
    else:
        singup_form=SingUpForm()
    return render(rq,"singup.html",{"form": singup_form,})


@login_required
def profile(rq):
    return render(rq,"profile.html")



def user_logout(rq):
    logout(rq)
    messages.success(rq,"Logout Succesfully")
    return redirect ("login")


def user_login(rq):
    form=AuthenticationForm(rq,rq.POST)
    if form.is_valid():
        user_name = form.cleaned_data["username"]
        user_pass = form.cleaned_data["password"]
        user = authenticate(username=user_name, password=user_pass)
        if user is not None:
            login(rq,user)
            messages.success(rq,"Login Succesfully")
            return redirect("profile")
        else:
            messages.warning(rq, "Login info Incorrect")
            return redirect("singup")
    else:
        form = AuthenticationForm()
        return render(rq, "login.html", {"form": form})
    
    
@login_required    
def password(rq):
    return render(rq,"password.html")   


@login_required
def pass_change(rq):
    if rq.method == "POST":
        form=PasswordChangeForm(rq.user,data=rq.POST)
        if form.is_valid():
            form.save()
            messages.success(rq,"Password Changed Successfully")
            update_session_auth_hash(rq,form.user)
            return redirect("profile")
    else:
        form=PasswordChangeForm(user=rq.user)
    return render(rq,"pass_change.html",{"form": form})    


@login_required
def pass_change_without_old(rq):
    if rq.method == "POST":
        form=SetPasswordForm(rq.user,data=rq.POST)
        if form.is_valid():
            form.save()
            messages.success(rq,"Password Changed Successfully")
            update_session_auth_hash(rq,form.user)
            return redirect("profile")
    else:
        form=SetPasswordForm(user=rq.user)
    return render(rq,"pass_change_without_old.html",{"form": form}) 