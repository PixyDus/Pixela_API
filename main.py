import requests
from datetime import datetime

# Setting up a User Account on Pixela.
pixels_endpoint = "https://pixe.la/v1/users"
TOKEN = "create your own token"
USERNAME = "create your username"
GRAPH_ID = "define your own graph ID"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixels_endpoint, json=user_params)
# print(response.text)

# Setting up Graph.
graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "GymHit Graph",
    "unit": "Hr",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response)

# Update a Pixel.
update_pixel_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_config = {
    "quantity": "1.30",}

response = requests.put(url=update_pixel_endpoint, json=new_pixel_config, headers=headers)
print(response.text)