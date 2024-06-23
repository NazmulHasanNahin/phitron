from django.shortcuts import render,redirect
from .import models
# Create your views here.


def home(rq):
    student=models.Student.objects.all()    
    return render(rq,"home.html",{"data":student})

def delete_stu(rq,roll):
    std=models.Student.objects.get(pk=roll).delete()
    return redirect("homepage")
    