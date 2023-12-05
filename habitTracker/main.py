import requests
from datetime import datetime

TOKEN = "Tester123"
USERNAME = "tjoshi"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "g1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response1 = requests.post(url=pixela_endpoint, json=user_params)
# print(response1.text)
#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Running graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response2.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2023, month=9, day=24)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.47",

}
# response3 = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response3.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
        "quantity": "5.47",

}

responseUpdated = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(responseUpdated.text)
