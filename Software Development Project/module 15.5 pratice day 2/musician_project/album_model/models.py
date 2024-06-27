from django.db import models
from musician_model.models import *
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=40)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)  #releted name chlo
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
