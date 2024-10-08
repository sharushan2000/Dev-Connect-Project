# Generated by Django 5.0.2 on 2024-03-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_handling', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
