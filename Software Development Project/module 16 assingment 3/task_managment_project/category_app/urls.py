from category_app.views import *
from django.urls import path,include

urlpatterns = [
    path("add/",category_add,name="category_add")
]
