from django.shortcuts import render

# Create your views here.


def home(request):
    d={"author" : "rahim" , "age" : 20}
    return render(request,"home.html",d)