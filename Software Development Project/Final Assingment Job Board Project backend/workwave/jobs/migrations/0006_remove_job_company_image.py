# Generated by Django 5.0.6 on 2024-08-08 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_company_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_image',
        ),
    ]