from posts.views import *
from django.urls import *

urlpatterns = [
    path("add/",add_post,name="add_post")
]
