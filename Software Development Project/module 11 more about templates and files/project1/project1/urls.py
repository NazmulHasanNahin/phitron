
from django.contrib import admin
from django.urls import *
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('firstapp/', include("firstapp.urls")),
]
