
from django.shortcuts import render
import requests
from users_handling.models import Project
from django.contrib.auth.models import User


def explore_home(request):
    url = ('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f7c1b07dcf77433cae42f0f3cc51ba38')

    try:
        # Making a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parsing the JSON response into a dictionary
            data = response.json()
            articles = data.get('articles', [])
        else:
            articles = []
            print("Failed to retrieve data, Status code:", response.status_code)

    except requests.RequestException as e:
        print("Error during requests to {0} : {1}".format(url, str(e)))
        articles = []

    # Render and return the response using the 'news_feed.html' template
    # and pass the articles to the template context
    return render(request, 'explore/explore_news.html', {'articles': articles})


# Define a view function to handle exploring users
def explore_users(request):

    if request.method == 'POST':

        search = request.POST.get('search_user', None)

        if search:
            # Filter users based on the search query
            users = User.objects.filter(username__contains=search)[0:10]
            return render(request, 'explore/explore_users.html', {'users_list': users})

    # Retrieve all users
    users = User.objects.all()

    return render(request, 'explore/explore_users.html', {'users_list': users})


def explore_project(request):

    if request.method == 'POST':

        search = request.POST.get('search_project', None)

        if search:

            projects = Project.objects.filter(
                title__contains=search, user__userprofile__public=True)
            return render(request, 'explore/explore_project.html', {'projects': projects})

    projects = Project.objects.filter(user__userprofile__public=True)

    return render(request, 'explore/explore_project.html', {'projects': projects})
