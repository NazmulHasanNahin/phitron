# jobs/serializers.py
from rest_framework import serializers
from .models import Job, JobCategory

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'location', 'experience', 'employee_type', 'position', 'offer_salary', 'responsibilities', 'qualifications', 'skills_experience']
        


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ('id','name',)
