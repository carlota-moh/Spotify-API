from secrets import *
import json
import base64
import requests
from requests.auth import HTTPBasicAuth

# Request authorization from user

auth_url = "https://accounts.spotify.com/authorize"
redirect_uri = "https://jpn-top-100.com/callback"

params = {"client_id": client_id,
          "response_type": "code",
          "redirect_uri": redirect_uri,
          "scope": "playlist-modify-public"}

response = requests.get(auth_url, params=params) 

print("Please authorize app using this URL: " + response.url)
redirect_response = input("\n\nPaste the URL you are being redirected to here: ")

code = re.search("code(.*)", redirect_response)

# Get access token

token_url = "https://accounts.spotify.com/api/token"

encoded64 = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

data = {
     "grant_type": "authorization_code",

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