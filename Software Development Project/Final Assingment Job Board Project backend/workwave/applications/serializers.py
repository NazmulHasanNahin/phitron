# applications/serializers.py
from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','job', 'job_seeker', 'resume', 'cover_letter']
