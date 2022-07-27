import requests
from datetime import datetime

TOKEN = None # Put your token here!
USERNAME = None # Put your username here!
GRAPH_ID = None # Name your graph here!

# Creating an account on pixela
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Creating a Graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "ichou",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Creating a Pixel
post_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many minutes did you put on coding today?! "),
}

response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Updating an existing Pixel
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_new_data = {
    "quantity": "150",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_new_data, headers=headers)
# print(response.text)

# Deleting an existing Pixel
pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
