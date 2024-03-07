from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
#build in login 
def login(request):
    return render(request ,'users_handling/login.html' ,{})

def register(request):
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created successfully. Please log in.')
            return redirect('home:home')
        else:
            # Form is not valid, so render the form again with validation errors
            messages.error(request, 'Please correct the error below.')
    else:
        if request.user.is_authenticated:
            return redirect('home:home')
        form = RegisterForm()
    
    # This return statement will handle both new (GET) requests and invalid (POST) submissions
    return render(request, 'users_handling/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request) # This will log out the user
    return redirect('home:home') # Redirect to the home page

def myprofile(request,username):
    id = request.user.id
    my = User.objects.get(id=id)
    return render(request ,'users_handling/user_profile.html' ,{'my':my}) # This will render the profile page