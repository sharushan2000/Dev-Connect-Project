from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile,ContactInformation
from django.contrib.auth.models import User
# build in login


def login(request):
    return render(request, 'users_handling/login.html', {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}, your account has been created successfully. Please log in.')
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
    logout(request)  # This will log out the user
    return redirect('home:home')  # Redirect to the home page


@login_required
def myprofile(request, username):
    my_username = request.user.username
    id = request.user.id
    my_contact = None
    value =True
    if username != my_username:
        redirect('home:home')
    if hasattr(request.user, 'contactinformation'):
        my_contact = request.user.contactinformation
    print(my_contact)
    if my_contact is None:
        value = False
    my = User.objects.get(id=id)
    # This will render the profile page
    return render(request, 'users_handling/user_profile.html', {'my': my ,'value':value, 'my_contact': my_contact})


@login_required
def showprofile(request, id, username):
    # print(username)
    profile = User.objects.get(id=id)

    # print(profile.userprofile)
    # print(request.user.userprofile.follows.all())
    if profile == request.user:
        return redirect('users_handling:myprofile', username)
    if request.method == "POST":
        showing_user_userprofile = profile.userprofile
        current_user_userprofile = request.user.userprofile

        # getting form value
        action = request.POST['isfollow']

        if action == "unfollow":
            current_user_userprofile.follows.remove(showing_user_userprofile)
        elif action == "follow":
            current_user_userprofile.follows.add(showing_user_userprofile)

        current_user_userprofile.save()

    if profile.userprofile in request.user.userprofile.follows.all():
        follow = False
    else:
        follow = True

    # This will render the profile page
    return render(request, 'users_handling/other_user.html', {'profile': profile, 'name': username, 'follow': follow})


@login_required
def following_list(request, id):
    user = User.objects.get(id=id)
    # following_users = user.userprofile.follows.all()
    # print(following_users)
    # This will render the profile page
    return render(request, 'users_handling/following_list.html', {'user': user})


def followers_list(request, id):
    user = User.objects.get(id=id)

    # This will render the profile page
    return render(request, 'users_handling/followers_list.html', {'user': user})

@login_required
def connect(request):
    profile_list = UserProfile.objects.filter(public=True).exclude(user=request.user)
    print(profile_list)

    return render(request, 'users_handling/connect.html', {"profile_list": profile_list})