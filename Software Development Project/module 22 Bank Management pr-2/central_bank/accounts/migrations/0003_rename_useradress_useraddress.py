# Generated by Django 5.0.6 on 2024-07-08 16:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_contry_useradress_country_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAdress',
            new_name='UserAddress',
        ),
    ]