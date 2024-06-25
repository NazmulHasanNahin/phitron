from django.shortcuts import render,redirect
from posts.forms import *
# Create your views here.


def add_post(rq):
    if rq.method == "POST":
        post_form=PostForm(rq.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")
    else:
        post_form=PostForm() 
    return render(rq,"add_post.html",{"form": post_form})