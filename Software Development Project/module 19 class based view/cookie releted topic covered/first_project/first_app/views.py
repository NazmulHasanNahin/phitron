from django.shortcuts import render

# Create your views here.

def home(request):
    response=render(request,"home.html")
    response.set_cookie("name","nahin")
    return response