# Generated by Django 5.0.6 on 2024-06-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0002_remove_category_tasks'),
        ('task_app', '0003_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='category_app.category'),
        ),
    ]