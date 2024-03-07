from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model): # This is the model for the user profile   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     symmetrical=False,
                                     related_name="followed_by",
                                     blank=True)
    # bio = models.CharField(max_length=100, blank=True)
    # profile_pic = models.ImageField(default='profile_pic.png' ,upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    

#create profile when user created
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_obj = UserProfile(user=instance)

        user_obj.save()
        user_obj.follows.set([instance.userprofile.id])# This will make the user follow themselves
        user_obj.save()


post_save.connect(create_profile,sender=User) # This will create a user profile when a new user is created