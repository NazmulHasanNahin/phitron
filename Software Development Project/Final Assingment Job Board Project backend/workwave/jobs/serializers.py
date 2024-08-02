# jobs/serializers.py
from rest_framework import serializers
from .models import Job, JobCategory

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ('id','name',)
