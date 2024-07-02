from django.shortcuts import render,redirect
from posts.models import *
from catagories.models import Catagory

def home(rq,catagory_slug=None):
    data=Posts.objects.all()
    if catagory_slug is not None:
        catagory=Catagory.objects.get(slug=catagory_slug)
        data=Posts.objects.filter(category=catagory)
    
    catagories=Catagory.objects.all()
    return render(rq,"home.html",{'data' : data,"catagory":catagories})


