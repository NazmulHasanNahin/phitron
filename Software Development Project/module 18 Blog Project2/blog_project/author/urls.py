from author.views import *
from django.urls import *

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path("profile/",profile,name="profile"),
    path("profile/edit",edit_profile,name="edit_profile"),
    path("profile/edit/pass_change/",pass_change,name="pass_change"),
]
