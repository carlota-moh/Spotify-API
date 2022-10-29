from secrets import *
import json
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

redirect_uri = 'https://jpn-top-100.com/callback' 

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

scope = ["playlist-modify-public"]

spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

authorization_url, state = spotify.authorization_url(auth_url)
print('Authorize using this link: ', authorization_url)

redirect_response = input('\n\nPaste the full redirect URL here: ')

print("\n")

# Fetch the access token

auth = HTTPBasicAuth(client_id, client_secret) 

token = dict(spotify.fetch_token(token_url, auth=auth,
        authorization_response=redirect_response))
        
print(f'This is your token: {token}')

# Save to JSON

with open("token.json", "w") as file:
    json.dump(token, file)
