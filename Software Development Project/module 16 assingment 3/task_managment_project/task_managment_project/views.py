from django.shortcuts import render,redirect

def home(rq):
    return render(rq,"home.html")