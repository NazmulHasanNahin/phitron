
from django.urls import *
from .import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
    path('form_submit/', views.form_submit,name="form_submit"),
    path('django_form/', views.StudentForm,name="django_form"),
]
