from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>This is Home page of django</h1>")


def contact(request):
    return HttpResponse("<h1>This is contact page of django</h1>")
