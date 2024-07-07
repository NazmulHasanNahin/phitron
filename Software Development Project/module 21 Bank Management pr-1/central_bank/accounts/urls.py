from django.urls import path
from accounts.views import *

urlpatterns = [
    path("register/",UserRegistrationView.as_view(),name="register"),
    
]
