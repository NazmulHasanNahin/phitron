from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def add_post(rq):
    if rq.method == "POST":
        post_form=forms.PostForm(rq.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")
    else:
        post_form=forms.PostForm() 
    return render(rq,"add_post.html",{"form": post_form})




def edit_post(rq, id):
    post = forms.Posts.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    if rq.method == 'POST':
        post_form = forms.PostForm(rq.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    
    return render(rq, 'add_post.html', {'form' : post_form})

def delete_post(rq,id):
    post = forms.Posts.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
    