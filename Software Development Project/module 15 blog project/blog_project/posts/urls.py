from posts.views import *
from django.urls import *

urlpatterns = [
    path("add/",add_post,name="add_post"),
    path("edit/<int:id>",edit_post,name="edit_post"),
    path("delete/<int:id>",delete_post,name="delete_post"),
]
