from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users_handling"

urlpatterns = [
    path('register/', views.register, name="signup"),
    
    # Using Django's built-in LoginView for the login page
    path('login/', auth_views.LoginView.as_view(template_name='users_handling/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('connect/', views.connect, name="connect"),
    path('profile/<str:username>/', views.myprofile, name="myprofile"),
    path('profile/<int:id>/following/', views.following_list, name="following_list"),
    path('profile/<int:id>/followers/', views.followers_list, name="followers_list"),
    path('profile/<int:id>/<str:username>/', views.showprofile, name="showprofile"),
    path('profile/edit/contact', views.edit_contact, name="edit_contact"),
    path('profile/contact/update/', views.update_contact, name="update_contact"),
    path('profile/add/project/', views.add_project, name="add_project"),
    path('profile/update/project/<int:id>/', views.update_project, name="update_project"),
]