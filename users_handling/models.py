from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model): # This is the model for the user profile   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     symmetrical=False,
                                     related_name="followed_by",
                                     blank=True)
    public = models.BooleanField(default=True)
    bio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(default='profile_pic.png' ,upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    
class ContactInformation(models.Model): # This is the model for the contact information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    github = models.URLField(blank=True)
    phone = models.CharField(max_length=15 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    city = models.CharField(max_length=50 ,blank=True)
    state = models.CharField(max_length=50 ,blank=True)
    country = models.CharField(max_length=50 ,blank=True)

    def __str__(self):
        return self.user.username + " contact information"

class Project(models.Model): # This is the model for the project
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    git_url = models.URLField(blank=True)
    date = models.DateField()
    likes = models.ManyToManyField(User, related_name='likes_by', blank=True)
    # dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    def __str__(self):
        return self.title + self.user.username
    


#create profile when user created
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_obj = UserProfile(user=instance)

        user_obj.save()
        user_obj.follows.set([instance.userprofile.id])# This will make the user follow themselves
        user_obj.save()


post_save.connect(create_profile,sender=User) # This will create a user profile when a new user is created