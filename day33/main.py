import requests
from datetime import datetime
import smtplib

MY_LAT = 49.162781
MY_LONG = -123.136650
my_email = "joshitrigun5@gmail.com"
password = "tpqyqequnoushney"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
# https://api.sunrise-sunset.org/json?lat=49.162781&lng=-123.136650

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(type(sunrise), sunset)

time_now = datetime.now()
print("now", time_now.hour)