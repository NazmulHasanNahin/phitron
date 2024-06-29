from author.views import *
from django.urls import *

urlpatterns = [
    path("register/",register,name="register")
]
