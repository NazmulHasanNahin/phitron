from django.shortcuts import render,redirect
from author.forms import *
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
            return redirect("register")
    else:
        register_form=RegistrationForm() 
    return render(rq,"register.html",{"form": register_form})