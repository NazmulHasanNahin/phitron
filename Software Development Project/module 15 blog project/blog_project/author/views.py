from django.shortcuts import render,redirect
from author.forms import *
# Create your views here.

def add_authors(rq):
    if rq.method=="POST":
        author_form=AuthorForm(rq.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("add_authors")
    else:
        author_form=AuthorForm() 
    return render(rq,"add_author.html",{"form": author_form})