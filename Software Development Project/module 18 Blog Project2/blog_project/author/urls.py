from author.views import *
from django.urls import *

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",user_login,name="login"),
]
