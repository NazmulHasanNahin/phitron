from django.db import models
from catagories.models import *
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Catagory)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="posts/media/uploads/",blank=True,null=True)
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=20)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name