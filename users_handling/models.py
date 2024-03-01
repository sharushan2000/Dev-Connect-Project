from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model): # This is the model for the user profile   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(default='profile_pic.png' ,upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    



