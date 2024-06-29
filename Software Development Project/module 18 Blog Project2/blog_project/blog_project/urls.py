
from django.contrib import admin
from django.urls import *
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="homepage"),
    path("author/",include("author.urls")),
    path("catagory/",include("catagories.urls")),
    path("post/",include("posts.urls")),
]
