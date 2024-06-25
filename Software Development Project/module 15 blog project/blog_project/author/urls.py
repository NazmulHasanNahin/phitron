from author.views import *
from django.urls import *

urlpatterns = [
    path("add/",add_authors,name="add_authors")
]
