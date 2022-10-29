# Refresh token
import requests
import json

# Make requests

with open('token.json') as json_file:
    token = json.load(json_file)

access = token['access_token']

url = 'https://api.spotify.com/v1' # Spotify Web API

art_id = '6mEQK9m2krja6X1cfsAjfl'

artist_url = f'{url}/artists/{art_id}'

album_url = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'

headers = {'Authorization': 'Bearer '+access}

response = requests.get(artist_url, headers=headers)

print(response.json())