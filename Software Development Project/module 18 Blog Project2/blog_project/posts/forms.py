from django import forms
from posts.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields = ['title','content','category','author']