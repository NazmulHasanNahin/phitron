from django.db import models
from catagories.models import *
from author.models import *
# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Catagory)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title