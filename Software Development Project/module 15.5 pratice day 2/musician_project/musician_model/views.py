from django.shortcuts import render,redirect
from musician_model.models import *
from musician_model.forms import *

# Create your views here.

def musician_list(rq):
    musicians=Musician.objects.all()
    return render(rq,"musician_list.html",{'musicians': musicians})


def musician_create(rq):
    if rq.method == "POST":
        form=MusicianForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm()
    return render(rq,'musician_form.html', {'form': form})


def musician_update(rq,id):
    musician=Musician.objects.get(pk=id)
    if rq.method=="POST":
        form = MusicianForm(rq.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(rq, 'musician_form.html', {'form': form})


def musician_delete(rq, id):
    musician = Musician.objects.get(pk=id)
    if rq.method == 'POST':
        musician.delete()
        return redirect('musician_list')
    return render(rq, 'musician_confirm_delete.html', {'musician': musician})