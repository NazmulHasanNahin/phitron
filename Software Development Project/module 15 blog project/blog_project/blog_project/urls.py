
from django.contrib import admin
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("author/",include("author.urls")),
    path("catagory/",include("catagories.urls")),
    path("post/",include("posts.urls")),
    path("profile/",include("profiles.urls")),
]
