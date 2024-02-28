
from django.urls import path
from . import views

app_name = 'home' #use this name as reference in html tagging - sk

urlpatterns = [
    path('',views.home , name="home"),


]
