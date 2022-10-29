from secrets import *
import json
import base64
from urllib import response
import requests
from requests.auth import HTTPBasicAuth

with open('token.json') as json_file:
    token = json.load(json_file)

token_url = "https://accounts.spotify.com/api/token"

encoded64 = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

data = {'grant_type': 'client_credentials',
        'refresh_token': token}

headers = {
     "Content-Type": "application/x-www-form-urlencoded",
     "Authorization": "Basic " + encoded64
}

response = requests.post(token_url, data=data, headers=headers)

print(response.json())

with open("token.json", "w") as file:
    json.dump(token, file)

