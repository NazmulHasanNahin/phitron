# Generated by Django 5.0.6 on 2024-07-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useradress',
            old_name='contry',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='useradress',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
