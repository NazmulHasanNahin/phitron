from django.urls import path
from story_app.views import *

urlpatterns = [
    path("profile/",profile,name="profile"),
    path("singup/",singup,name="singup"),
    path("logout/",user_logout,name="logout"),
    path("login/",user_login,name="login"),
    path("password_change/",password,name="password"),
    path("password_change/with_old_pass",pass_change,name="pass_change"),
    path("password_change/without_old_pass",pass_change_without_old,name="pass_change_without_old"),
]
