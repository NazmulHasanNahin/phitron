from django.urls import path,include
from first_app.views import *

urlpatterns = [
    path("",home,name="homepage"),
    path("singup/",singup,name="singup"),
    path("login/",user_login,name="login"),
    path("profile/",profile,name="profile"),
    path("logout/",user_logout,name="logout"),
    path("pass_change/",pass_change,name="pass_change"),
    path("pass_change_without_old/",pass_change_without_old,name="pass_change_without_old"),
    
]
