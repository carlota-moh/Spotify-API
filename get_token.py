from secrets import *
import json
import base64
import requests
from requests.auth import HTTPBasicAuth

token_url = "https://accounts.spotify.com/api/token"

encoded64 = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

data = {
     "grant_type": "client_credentials"
}

headers = {
     "Content-Type": "application/x-www-form-urlencoded",
     "Authorization": "Basic " + encoded64
}

response = requests.post(token_url, data=data, headers=headers)

print(response.json())

token = response.json()

with open("token.json", "w") as file:
    json.dump(token, file)