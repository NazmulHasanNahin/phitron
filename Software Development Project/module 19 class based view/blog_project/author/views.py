from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from author.forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import *
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.



def register(rq):
    if rq.method == "POST":
        register_form = RegistrationForm(rq.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(rq, "Account Registred Successfully")
            return redirect("register")
    else:
        register_form = RegistrationForm()
    return render(rq, "register.html", {"form": register_form, "type": "Register"})


def user_login(rq):
    if rq.method == "POST":
        form = AuthenticationForm(rq, rq.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(rq, user)
                messages.success(rq, "Login Successfully")
                return redirect("profile")
            else:
                messages.warning(rq, "Login info Incorrect")
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(rq, "register.html", {"form": form, "type": "Login"})
    
#class based view

class UserLoginView(LoginView):
    template_name="register.html"
    # success_url=reverse_lazy("profile")
    def get_success_url(self) -> str:
        return reverse_lazy("profile")
    
    def form_valid(self, form):
        messages.success(self.request,"Login Succesfull")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,"Login Unsuccesfull")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["type"]="Login"
        return context

@login_required
def profile(rq):
    data = Posts.objects.filter(author=rq.user)
    return render(rq,"profile.html",{"data":data})


@login_required    
def edit_profile(rq):
    if rq.method=="POST":
        profile_form=ChnageUserForm(rq.POST,instance=rq.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(rq,"Profile Updated Successfully")
            return redirect("profile")
    else:
        profile_form=ChnageUserForm(instance=rq.user) 
    return render(rq,"update_profile.html",{"form": profile_form})



def pass_change(rq):
    if rq.method=="POST":
        form=PasswordChangeForm(rq.user,data=rq.POST)
        if form.is_valid():
            form.save()
            messages.success(rq,"Password Changed Successfully")
            update_session_auth_hash(rq,form.user)
            return redirect("profile")
    else:
        form=PasswordChangeForm(user=rq.user) 
    return render(rq,"pass_change.html",{"form": form})


def user_logout(rq):
    logout(rq)
    return redirect("login")