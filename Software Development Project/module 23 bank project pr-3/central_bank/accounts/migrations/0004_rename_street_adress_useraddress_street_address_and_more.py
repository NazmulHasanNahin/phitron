# Generated by Django 5.0.6 on 2024-07-08 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_useradress_useraddress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='street_adress',
            new_name='street_address',
        ),
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='initial_deposit_date',
            new_name='initial_deposite_date',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
