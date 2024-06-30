from django.shortcuts import render,redirect
from author.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

# def add_authors(rq):
#     if rq.method=="POST":
#         author_form=AuthorForm(rq.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect("add_authors")
#     else:
#         author_form=AuthorForm() 
#     return render(rq,"add_author.html",{"form": author_form})



def register(rq):
    if rq.method=="POST":
        register_form=RegistrationForm(rq.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(rq,"Account Registred Successfully")
            return redirect("register")
    else:
        register_form=RegistrationForm() 
    return render(rq,"register.html",{"form": register_form,"type":"Register"})


def user_login(rq):
    if rq.method=="POST":
        form=AuthenticationForm(rq,rq.POST)
        if form.is_valid():
            user_name=form.cleaned_data["username"]
            user_pass=form.cleaned_data["password"]
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                login(rq,user)
                messages.success(rq,"Login Successfully")
                return redirect("login")
            else:
                messages.warning(rq,"Login info Incorrect")
                return redirect("register")
    else:
        form=AuthenticationForm()
        return render(rq,"register.html",{"form": form,"type":"Login"})