from django.urls import path,include
from pratice_app.views import *

urlpatterns = [
    path("",home,name="home")
]
