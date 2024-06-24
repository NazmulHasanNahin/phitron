from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=20)
    bio=models.TextField(max_length=200)
    phone=models.IntegerField(max_length=11)
    
    def __str__(self):
        return self.name