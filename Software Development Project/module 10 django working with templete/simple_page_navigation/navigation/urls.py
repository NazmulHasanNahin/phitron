from django.urls import *
from .import views
urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact),
    
]
