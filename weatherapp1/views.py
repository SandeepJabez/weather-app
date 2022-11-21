from django.shortcuts import render

# Create your views here.

import requests


def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8514de72e4d5cb7523fb502496a62a71'

    city1 = 'Pune'
    city2 = 'Mumbai'
    city3 = 'Delhi'

    # we are requesting the API data and converting the JSON to Python data types
    city_weather = requests.get(url.format(city1)).json()
    print(city_weather)  # checking the output
    weather = {
        'city': city1,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
        'humidity': city_weather['main']['humidity'],
        'wind': city_weather['wind']['speed'],
        "feels_like": city_weather['main']['feels_like'],
        'pressure': city_weather['main']['pressure']

    }
    city_weather2 = requests.get(url.format(city2)).json()
    weather1 = {
        'city': city2,
        'temperature': city_weather2['main']['temp'],
        'description': city_weather2['weather'][0]['description'],
        'icon': city_weather2['weather'][0]['icon'],
        'humidity': city_weather2['main']['humidity'],
        "feels_like": city_weather2['main']['feels_like'],
        'wind': city_weather2['wind']['speed'],
        'pressure': city_weather2['main']['pressure']

    }

    city_weather3 = requests.get(url.format(city3)).json()
    weather3 = {
        'city': city3,
        'temperature': city_weather3['main']['temp'],
        'description': city_weather3['weather'][0]['description'],
        'icon': city_weather3['weather'][0]['icon'],
        'humidity': city_weather3['main']['humidity'],
        "feels_like": city_weather3['main']['feels_like'],
        'wind': city_weather3['wind']['speed'],
        'pressure': city_weather3['main']['pressure']
    }
    print("********************")
    print(city_weather2)
    print("********************")
    print(city_weather3)
    context = {'weather': weather, 'weather1': weather1,'weather3': weather3}
    # returns the index.html template
    return render(request, 'weather/index.html', context)
