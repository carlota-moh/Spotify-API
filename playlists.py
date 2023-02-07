import json
import base64
import requests

def call_endpoint(url, token):
      headers = {"Authorization": "Bearer "+token,
                "Content-Type": "application/json"}

      response = requests.get(url, headers=headers)

      if response.status_code == 200:
            print("Successfully retrieved playlist")
            playlists = response.json()
            return playlists
      else:
            print("Something went wrong! Response status code: %s" % response.status_code)

def read_playlists(user_id, token):
      url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

      playlists = call_endpoint(url=url, token=token)

      return playlists['items']

def read_playlist(user_id, token, playlist_id):

      url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}"

      playlist = call_endpoint(url=url, token=token)

      return playlist

def make_playlist():
      pass

