from django.contrib import admin
from django.urls import *
# from views import contact

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage),
    path("first_app/",include("first_app.urls")),
    path('contact/',views.contact),
]
