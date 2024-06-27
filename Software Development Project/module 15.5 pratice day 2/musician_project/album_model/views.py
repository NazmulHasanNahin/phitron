from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def album_list(rq):
    albums = Album.objects.all()
    return render(rq, 'album_list.html', {'albums': albums})

def album_create(rq):
    if rq.method == 'POST':
        form = AlbumForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(rq, 'album_form.html', {'form': form})

def album_update(rq, id):
    album = Album.objects.get(pk=id)
    if rq.method == 'POST':
        form = AlbumForm(rq.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(rq, 'album_form.html', {'form': form})

def album_delete(rq, id):
    album = Album.objects.get(pk=id)
    if rq.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(rq, 'album_confirm_delete.html',)  # {'album': album}
