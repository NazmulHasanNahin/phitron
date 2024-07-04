from django.urls import path
from car_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',car_list_view, name='car-list'),
    path('car/<int:pk>/', car_detail_view, name='car-detail'),
    path('buy/<int:pk>/', buy_car_view, name='buy-car'),
    path('add-brand/', AddBrandView.as_view(), name='add-brand'),
    path('add-car/',AddCarView.as_view(), name='add-car'),
    path('order-history/',order_history_view, name='order-history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
