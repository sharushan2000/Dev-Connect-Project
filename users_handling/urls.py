
from django.urls import path
from . import views

app_name = "users_handling"

urlpatterns = [
    path('login/' , views.login , name= "login"),
    path('signup/' , views.signup , name= "signup"),

]
