from django.shortcuts import render, redirect
from . import forms
from . import models
from posts.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_post(rq):
    if rq.method == "POST":
        post_form=forms.PostForm(rq.POST)
        if post_form.is_valid():
            # post_form.cleaned_data["author"]=rq.user
            post_form.instance.author=rq.user
            post_form.save()
            return redirect("add_post")
    else:
        post_form=forms.PostForm() 
    return render(rq,"add_post.html",{"form": post_form})



@login_required
def edit_post(rq, id):
    post = forms.Posts.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    if rq.method == 'POST':
        post_form = forms.PostForm(rq.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author=rq.user
            post_form.save()
            return redirect('homepage')
    
    return render(rq, 'add_post.html', {'form' : post_form})


@login_required
def delete_post(rq,id):
    post = forms.Posts.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
    