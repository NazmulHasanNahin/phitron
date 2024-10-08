# Generated by Django 5.0.6 on 2024-09-17 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('users', '0002_useraccount_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdashboard',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount'),
        ),
        migrations.AlterField(
            model_name='sellerdashboard',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount'),
        ),
    ]
