from django.db import models
from django import forms
from .models import ExampleModel, MyModel
class ExampleModel(models.Model):
    comment = models.TextField(max_length=200)

#     def __str__(self):
#         return self.comment


# class ExampleModel(models.Model):
#     agree = models.BooleanField()

#     def __str__(self):
#         return self.agree


# class ExampleModel(models.Model):
#     date = models.DateField()


# class ExampleModel(models.Model):
#     email_address = models.EmailField()
    
# FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]
# class ExampleModel(models.Model):
#     favorite_color = models.CharField(max_length=10, choices=FAVORITE_COLORS_CHOICES)
    
    
FAVORITE_COLORS_CHOICES = [
    ('Gray', 'Gray'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleModel(models.Model):
    favorite_color = models.CharField(max_length=20,choices=FAVORITE_COLORS_CHOICES)
    
    
