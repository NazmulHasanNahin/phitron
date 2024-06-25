from django.shortcuts import render,redirect
from catagories.forms import *
# Create your views here.


def add_categories(rq):
    if rq.method == "POST":
        category_form=CategoryForm(rq.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("add_categories")
    else:
        category_form=CategoryForm() 
    return render(rq,"add_category.html",{"form": category_form})