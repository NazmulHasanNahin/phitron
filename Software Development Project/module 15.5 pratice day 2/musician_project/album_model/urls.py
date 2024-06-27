from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('create/', views.album_create, name='album_create'),
    path('update/<int:id>/', views.album_update, name='album_update'),
    path('delete/<int:id>/', views.album_delete, name='album_delete'),
]
