from django.contrib import admin
from .models import UserProfile
# Register your models here.


admin.site.register(UserProfile) # This line will make the UserProfile model visible on the admin page