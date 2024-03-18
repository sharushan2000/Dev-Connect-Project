from django.urls import path
from . import views



app_name = 'explore'

urlpatterns = [
    path('', views.explore_home, name='explore_home'),
    # Add more paths here as needed
]