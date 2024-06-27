from django.db import models

class Task(models.Model):
    from category_app.models import Category
    task_title = models.CharField(max_length=40)
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    task_assigned_dt = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.task_title

