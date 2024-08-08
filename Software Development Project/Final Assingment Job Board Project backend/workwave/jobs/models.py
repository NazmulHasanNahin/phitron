from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    employer = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE)
    company_image = models.ImageField(upload_to='companies/images/', null=True, blank=True)
    company_name = models.CharField(max_length=30)
    experience = models.CharField(max_length=255)
    employee_type = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    offer_salary = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    responsibilities = models.TextField()
    qualifications = models.TextField()
    skills_experience = models.TextField()

    def __str__(self):
        return self.title

class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
