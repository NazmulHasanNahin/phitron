from django.shortcuts import render


def home_page(rq):
    return render(rq,"base.html")