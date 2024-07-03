from django.urls import path
from first_app.views import *

urlpatterns = [
    path("",home,name="homepage")
]
