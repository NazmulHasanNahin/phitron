from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse("<h1>This is courses page of django</h1>")


def about(request):
    return HttpResponse("about section")


def home(request):
    return HttpResponse("home page of first app ")



