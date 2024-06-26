# Generated by Django 5.0.2 on 2024-04-06 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_handling', '0015_alter_userprofile_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Geek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geek_body', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geeks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
