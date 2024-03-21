from django.urls import path
from . import views



app_name = 'explore'

urlpatterns = [
    path('', views.explore_home, name='explore_home'),
    path('project/', views.explore_project, name='explore_project'),
    path('users/', views.explore_users, name='explore_users'),
    # Add more paths here as needed
]