import json
import base64
import requests

def get_request(url, token, params=None):

      headers = {"Authorization": "Bearer "+token,
                "Content-Type": "application/json"}

      response = requests.get(url, headers=headers, params=params)

      if response.status_code == 200:
            print("Successful get request")
            return response.json()

      else:
            print("Something went wrong! Response status code: %s" % response.status_code)

def post_request(url, token, data):
       
      headers = {"Authorization": "Bearer "+token,
                  "Content-Type": "application/json"}

      response = requests.post(url, headers=headers, data=data)

      if response.status_code == 200:
            print("Successful post request")
            return response.json()

      else:
            print("Something went wrong! Response status code: %s" % response.status_code)

def read_playlists(user_id, token):
      url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

      playlists = get_request(url=url, token=token)

      return playlists['items']

def read_playlist(user_id, token, playlist_id):

      url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}"

      playlist = get_request(url=url, token=token)

      return playlist

def make_playlist(user_id, token, playlist_name, playlist_description = None):

      url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

      data = json.dumps({"name": playlist_name,
                        "description": playlist_description,
                        "public": "true"}, indent=4)

      response = post_request(url=url, token=token, data=data)

      return response

def add_songs(user_id, token, playlist_id, uris):

      url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"

      data = json.dumps({"uris": uris}, indent=4)

      response = post_request(url=url, token=token, data=data)

      return response

def search_(query, type, limit, token):
      url = "https://api.spotify.com/v1/search"

      params = {"q": query,
               "type": type,
               "limit": limit}

      result = get_request(url=url, token=token, params=params)

      return result['items']

def search_song(query, limit, token):
      song_json = search_(query=query, type="track", limit=1, token=token)

      song_id = song_json['tracks']['items'][0]['id']

      return song_id



