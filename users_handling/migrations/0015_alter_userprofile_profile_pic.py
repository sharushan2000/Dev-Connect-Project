# Generated by Django 5.0.2 on 2024-03-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_handling', '0014_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.png', upload_to='profile_pics'),
        ),
    ]
