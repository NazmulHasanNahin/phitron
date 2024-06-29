from django.urls import path,include
from first_app.views import *

urlpatterns = [
    path("",home,name="homepage"),
    path("singup/",singup,name="singup"),
    path("login/",user_login,name="login"),
    path("profile/",profile,name="profile"),
    path("logout/",user_logout,name="logout"),
    
]
