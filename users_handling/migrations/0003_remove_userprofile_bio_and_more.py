# Generated by Django 5.0.2 on 2024-03-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_handling', '0002_userprofile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
    ]
