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
    profile_pic = models.ImageField(default='default_profile_pic.png' ,upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username
    
class ContactInformation(models.Model): # This is the model for the contact information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    github = models.URLField(blank=True)
    phone = models.CharField(max_length=15 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    city = models.CharField(max_length=50 ,blank=True)
    zip = models.IntegerField(blank=True ,null=True)
    state = models.CharField(max_length=50 ,blank=True)
    country = models.CharField(max_length=50 ,blank=True)

    def __str__(self):
        return self.user.username + " contact information"

class Project(models.Model): # This is the model for the project
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created') 
    title = models.CharField(max_length=100)
    description = models.TextField()
    git_url = models.URLField(blank=True)
    linkdedin_url = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    collaborators = models.ManyToManyField(User, related_name='collobrators_for', blank=True)
    #likes = models.ManyToManyField(User, related_name='likes_by', blank=True)
    # dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    def __str__(self):
        return self.title + self.user.username
    
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_education')
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True , null=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.user.username + " " + self.degree + " " + self.school
    
    


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_experience')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True , null=True)
    

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.user.username + " " + self.title + " " + self.company

class Geek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='geeks')
    geek_body = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='geek_likes', blank=True)

    def __str__(self) -> str:
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )
    


#create profile when user created
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_obj = UserProfile(user=instance)

        user_obj.save()
        user_obj.follows.set([instance.userprofile.id])# This will make the user follow themselves
        user_obj.save()


post_save.connect(create_profile,sender=User) # This will create a user profile when a new user is created