# Generated by Django 5.0.6 on 2024-08-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='resume',
            field=models.FileField(upload_to='job_seekers/resumes/'),
        ),
    ]
