
from django.contrib import admin
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("first_app.urls")),
    
]
