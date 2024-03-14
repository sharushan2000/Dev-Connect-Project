from django.contrib import admin
from .models import UserProfile ,Project,ContactInformation ,Education
# Register your models here.


admin.site.register(UserProfile) # This line will make the UserProfile model visible on the admin page
admin.site.register(Project) # This line will make the Project model visible on the admin pageadmin
admin.site.register(ContactInformation) # This line will make the Project model visible on the admin page
admin.site.register(Education) # This line will make the Project model visible on the admin page