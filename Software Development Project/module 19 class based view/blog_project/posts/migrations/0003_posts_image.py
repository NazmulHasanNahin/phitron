# Generated by Django 5.0.6 on 2024-07-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
