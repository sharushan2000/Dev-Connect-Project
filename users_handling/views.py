from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Project ,Education,Experience
from django.contrib.auth.models import User
from .forms import RegisterForm , ContactInformationForm ,ProjectForm,EducationForm ,ExperienceForm

# build in login , authentication 
def login(request):
    return render(request, 'users_handling/login.html', {})


# This view function will handle the registration page
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}, your account has been created successfully. Please log in.')
            return redirect('users_handling:login')
        else:
            # Form is not valid, so render the form again with validation errors
            messages.error(request, 'Please correct the error below.')
    else:
        if request.user.is_authenticated:
            return redirect('home:home')
        form = RegisterForm()

    # This return statement will handle both new (GET) requests and invalid (POST) submissions
    return render(request, 'users_handling/register.html', {'form': form})

# This view function will handle the logout page
@login_required
def logout_view(request):
    logout(request)  # This will log out the user
    return redirect('home:home')  # Redirect to the home page

# show user profile
@login_required
def myprofile(request, username):
    my_username = request.user.username
    id = request.user.id
    my_contact = None
    education_history = None
    my_exeprience = None

    if hasattr(request.user ,'users_education'):
        education_history = request.user.users_education.all()
    if username != my_username:
        redirect('home:home')
    if hasattr(request.user, 'contactinformation'):
        my_contact = request.user.contactinformation
    # print(my_contact)
    if hasattr(request.user, 'users_experience'):
        my_exeprience = request.user.users_experience.all()
        print(my_exeprience)

    if hasattr(request.user, 'projects_created'):
        my_projects = request.user.projects_created.all()
        # print(my_projects)

    my = User.objects.get(id=id)
    # This will render the profile page
    return render(request, 'users_handling/my_resume.html', {'my': my ,
                                                                'my_contact': my_contact,
                                                                'my_projects': my_projects,
                                                                'history_of_education':education_history,
                                                                'my_exeprience': my_exeprience,})





# Add contact information 
@login_required
def edit_contact(request):
    if request.method == "POST":
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('users_handling:myprofile', request.user.username)
    else:
        form = ContactInformationForm()
    return render(request, 'users_handling/edit_contact.html', {'form': form})

# Update contact information
@login_required
def update_contact(request):

    contact = request.user.contactinformation
    form = ContactInformationForm(request.POST or None , instance=contact)
    if form.is_valid():
        form.save()
        return redirect('users_handling:myprofile', request.user.username)
    return render(request, 'users_handling/update_contact.html', {'form': form,'contact':contact})



# project views
@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Set the project's owner to the current user
            project.save()  # Save the project to generate an ID for M2M relationship
            project.collaborators.add(request.user)  # Add the user as a collaborator
            project.save()  # Save the project again, now with collaborators
            return redirect('users_handling:myprofile', request.user.username)
    else:
        form = ProjectForm()  # Provide an empty form for GET request

    return render(request, 'users_handling/add_project.html', {'form': form})

@login_required
def update_project(request,id):
    
    project = Project.objects.get(id=id)
    if project in request.user.projects_created.all():
        form = ProjectForm(request.POST or None , instance=project)
        if form.is_valid():
            form.save()
            return redirect('users_handling:myprofile', request.user.username)
        return render(request, 'users_handling/update_project.html', {'form': form,'project':project})
    else:
        return redirect('home:home')

@login_required  
def delete_project(request,id):
    project = Project.objects.get(id=id)
    if project in request.user.projects_created.all():
        project.delete()
        return redirect('users_handling:myprofile', request.user.username)
    else:
        return redirect('home:home')




# Education views
@login_required
def add_education(request):

    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('users_handling:myprofile', request.user.username)
    else:
        form = EducationForm()
    return render(request, 'users_handling/add_education.html', {'form': form})

@login_required
def education_history(request):
    history_of_education = request.user.users_education.all()
    return render(request, 'users_handling/education_history.html', {'history_of_education': history_of_education})

@login_required
def update_education(request,id):
    education = Education.objects.get(id=id)
    if education in request.user.users_education.all():

        form = EducationForm(request.POST or None , instance=education)
        if form.is_valid():
            form.save()
            return redirect('users_handling:myprofile', request.user.username)
        return render(request, 'users_handling/update_education.html', {'form': form,'education':education})
    
    else:
        return redirect('home:home')

@login_required
def delete_education(request,id):
    education = Education.objects.get(id=id)
    if education in request.user.users_education.all():
        education.delete()
        return redirect('users_handling:education_history')
    else:
        return redirect('home:home')





# This view function will handle the user profile page
@login_required
def showprofile(request, id, username):
    # print(username)
    profile = User.objects.get(id=id)
    contact = None
    projects = None
    if hasattr(profile,'contactinformation'):
        contact = profile.contactinformation
    if hasattr(profile, 'projects_created'):
        projects = profile.projects_created.all()

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
    return render(request, 'users_handling/user_profile.html', {'profile': profile, 
                                                                'name': username, 
                                                                'follow': follow, 
                                                                'contact': contact
                                                                ,'user_projects': projects})

# This view function will handle the user profile page
@login_required
def following_list(request, id):
    user = User.objects.get(id=id)
    # following_users = user.userprofile.follows.all()
    # print(following_users)
    # This will render the profile page
    return render(request, 'users_handling/following_list.html', {'user': user})

@login_required
def followers_list(request, id):
    user = User.objects.get(id=id)

    # This will render the profile page
    return render(request, 'users_handling/followers_list.html', {'user': user})

# This is the end of the views.py file


@login_required
def add_experience(request):
     
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('users_handling:myprofile', request.user.username)
        

    form = ExperienceForm()
    return render(request, 'users_handling/add_experience.html', {'form': form})

@login_required
def update_exeperience(request,id):
    experience = Experience.objects.get(id=id)
    if experience in request.user.users_experience.all():
        form = ExperienceForm(request.POST or None , instance=experience)
        if form.is_valid():
            form.save()
            return redirect('users_handling:myprofile', request.user.username)
        return render(request, 'users_handling/update_experience.html', {'form': form,'experience':experience})
    else:
        return redirect('home:home')