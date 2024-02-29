from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users_handling"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    
    # Using Django's built-in LoginView for the login page
    path('login/', auth_views.LoginView.as_view(template_name='users_handling/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
]