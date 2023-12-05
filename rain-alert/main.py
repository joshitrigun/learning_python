import requests

api_key = "6e886f6aa8869bd4be238e1c46abfeaf"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "lat": 37.935758,
    "lon": -123.11934,
    "appid": api_key
}

response = requests.get(BASE_URL, params=weather_parameters)


print(response.json())


#
# https://api.openweathermap.org/data/2.5/onecall?lat=49.24966&lon=-123.11934&appid=d8549e85b07f7fd08c81c02f26b162f9


# http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=d8549e85b07f7fd08c81c02f26b162f9

# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}