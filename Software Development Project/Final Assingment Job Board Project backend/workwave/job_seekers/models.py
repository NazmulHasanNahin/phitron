from django.db import models
from django.contrib.auth.models import User

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='job_seekers/resumes/')
    skills = models.TextField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    address = models.TextField() 
    country = models.CharField(max_length=50) 

    def __str__(self):
        return self.user.username
