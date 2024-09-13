from django.urls import path,include
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

urlpatterns = [
    path('', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('registration/', RegisterView.as_view(serializer_class=CustomRegisterSerializer), name='registration'),
]
