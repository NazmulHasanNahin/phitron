# Generated by Django 5.0.6 on 2024-08-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='random company name', max_length=30),
            preserve_default=False,
        ),
    ]
