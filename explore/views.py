
from django.shortcuts import render
import requests

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

