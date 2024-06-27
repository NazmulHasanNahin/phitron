from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('create/', views.musician_create, name='musician_create'),
    path('update/<int:id>/', views.musician_update, name='musician_update'),
    path('delete/<int:id>/', views.musician_delete, name='musician_delete'),
]
