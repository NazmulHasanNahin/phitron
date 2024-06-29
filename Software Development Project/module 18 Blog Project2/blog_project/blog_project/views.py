from django.shortcuts import render,redirect
from posts.models import *

def home(rq):
    data=Posts.objects.all()
    return render(rq,"home.html",{'data' : data})