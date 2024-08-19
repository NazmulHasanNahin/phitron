from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    job_seeker_name = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_seeker', 'job_seeker_name', 'resume', 'cover_letter']

    def get_job_seeker_name(self, obj):
        full_name = obj.job_seeker.get_full_name()
        if full_name.strip():
            return full_name
        return obj.job_seeker.username
