from django.shortcuts import render
from django.http import *
# Create your views here.


def home(rq):
    # return HttpResponse("This is home in first app")
    return render(rq,"first_app/home.html")

