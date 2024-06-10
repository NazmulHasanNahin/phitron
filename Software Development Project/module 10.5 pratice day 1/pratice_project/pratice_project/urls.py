from django.contrib import admin
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pratice/",include("app_pratice.urls")),
]
