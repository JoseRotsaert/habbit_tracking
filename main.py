import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": "Fdk6ZV*SMs84GYtZITpa",
#     "username": "josejuanzo",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
#     }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


USERNAME = "josejuanzo"
TOKEN = "Fdk6ZV*SMs84GYtZITpa"
GRAPH_ID = "graph1"


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
     "id": GRAPH_ID,
     "name": "Cycling Graph",
     "unit": "Km",
     "type": "float",
     "color": "ajisai"
 }

headers = {
     "X-USER-TOKEN": TOKEN
 }

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# https://pixe.la/v1/users/josejuanzo/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
print(pixel_creation_endpoint)

today = datetime.now()
today_yyyymmdd = today.strftime("%Y%m%d")
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today_yyyymmdd,
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
     "quantity": "4.5"
 }

# ## PUT
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
#
#
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
#
# ## DELETE
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)