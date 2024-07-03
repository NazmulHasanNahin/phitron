from django import forms
from posts.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        # fields = ['title','content','category','author']
        exclude=["author"]
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['name','email','body']