from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from posts.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
from posts.forms import PostForm,CommentForm
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

#add post using class based view

@method_decorator(login_required,name="dispatch")
class AddPostCreateView(CreateView):
    model=Posts()
    form_class=PostForm
    template_name="add_post.html"
    success_url=reverse_lazy("add_post")
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)





@login_required
def edit_post(rq, id):
    post = forms.Posts.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    if rq.method == 'POST':
        post_form = forms.PostForm(rq.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author=rq.user
            post_form.save()
            return redirect('profile')
    
    return render(rq, 'add_post.html', {'form' : post_form})

#edit post using class based view
@method_decorator(login_required,name="dispatch")
class EditPostView(UpdateView):
    model=Posts
    form_class=forms.PostForm
    template_name="add_post.html"
    pk_url_kwarg= "id"
    success_url=reverse_lazy("profile")
    
    
@method_decorator(login_required,name="dispatch")    
class DeletePostView(DeleteView):
    model=Posts
    template_name="delete.html"
    pk_url_kwarg= "id"
    success_url=reverse_lazy("profile")

@login_required
def delete_post(rq,id):
    post = forms.Posts.objects.get(pk=id) 
    post.delete()
    return redirect('profile')
    

class DetailsPostView(DetailView):
    model=Posts
    pk_url_kwarg="id"
    template_name="post_details.html"
    
    def post(self,request,*args,**kwargs):
            comment_form=CommentForm(data=self.request.POST)
            post=self.get_object()
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.post=post
                new_comment.save()
            return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=CommentForm()
            
        context["comments"]=comments
        context["comment_form"]=comment_form
        return context