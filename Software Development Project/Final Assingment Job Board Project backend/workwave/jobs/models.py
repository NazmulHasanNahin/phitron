from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    employer = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
