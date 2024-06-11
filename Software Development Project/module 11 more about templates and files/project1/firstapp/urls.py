
from django.urls import *
from .import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
]
