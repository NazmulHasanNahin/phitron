
from django.urls import *
from .import views

urlpatterns = [
    path("",views.home,name="homepage"),
    path("delete/<int:roll>",views.delete_stu,name="delete_student"),
    
]
