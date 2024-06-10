from .import views
from django.urls import *

urlpatterns = [
    path('',views.home),
]
