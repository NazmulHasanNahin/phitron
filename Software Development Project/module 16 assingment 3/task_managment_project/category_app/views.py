from django.shortcuts import render,redirect
from category_app.forms import *
# Create your views here.


def category_add(rq):
    if rq.method == "POST":
        form=CategoryForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect("category_add")
    else:
        form = CategoryForm()
    return render(rq,'category_add.html', {'form': form})
