
from django.contrib import admin
from django.urls import path,include
from core.views import *
urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls")),
    
]