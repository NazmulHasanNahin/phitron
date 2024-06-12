
from django.contrib import admin
from django.urls import *
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('', include("meal_app.urls")),
]
