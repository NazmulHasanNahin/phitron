from .import views
from django.urls import *

urlpatterns = [
    path("meal_details/",views.meal_details, name="meal_details")
]
