from rest_framework import serializers
from contact_us.models import *

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields="__all__"