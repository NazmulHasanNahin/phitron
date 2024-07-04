from django.urls import path
from django.shortcuts import render,redirect
from user_app.views import *
from django.conf import settings
from django.conf.urls.static import static
# urls

urlpatterns = [
    path("singup/",user_singup,name="singup"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout/",logoutView,name="logout"),
    path('edit-profile/', edit_profile_view, name='edit-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
