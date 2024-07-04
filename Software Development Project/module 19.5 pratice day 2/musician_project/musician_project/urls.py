from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("albums/",include("album_model.urls")),
    path("musicians/",include("musician_model.urls")),
]
