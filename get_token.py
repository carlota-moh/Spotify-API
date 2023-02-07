# Import dependencies
import base64
import requests
import re

def request_authorization(client_id, redirect_uri):
     """
     Function used to request authorization from user in order
     to access app
     
     INPUTS:
     -client_id: str
          Spotify client_id
     """
     # Request authorization from user
     auth_url = "https://accounts.spotify.com/authorize"

     params = {"client_id": client_id,
               "response_type": "code",
               "redirect_uri": redirect_uri,
               "scope": "playlist-modify-public"}

     response = requests.get(auth_url, params=params) 
     return response.url

def get_code(redirect_response):
     code = re.search("(?<=code=)\S+", redirect_response).group(0)
     return code

def encode_data(client_id, client_secret):
     # encode client_id and client_secret
     encoded64 = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
     return encoded64

def get_access_token(code, redirect_uri, encoded64):
     # Get access token
     token_url = "https://accounts.spotify.com/api/token"

     # Define data to be passed in the request body
     params = {"grant_type": "authorization_code",
               "code": code,
               "redirect_uri": redirect_uri}

     # Define request headers
     headers = {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": "Basic " + encoded64
     }

     # Call API
     response = requests.post(token_url, params=params, headers=headers)

     if response.status_code == 200:
          print("Successfully retrieved token")
          token_json = response.json()
          token = token_json['access_token']
          return token
     else:
          print("Something went wrong! Response status code: %s" % response.status_code)

def get_token():
     client_id = input("Please paste here your client id: ")
     client_secret = input("Please paste here your client secret: ")
     redirect_uri = "https://jpn-top-100.com/callback"
     response_url = request_authorization(client_id=client_id,
                                          redirect_uri=redirect_uri)
     print("Please authorize app using the following link: %s" % response_url)
     redirect_response = input("Paste the URL you are being redirected to here: ")
     code = get_code(redirect_response=redirect_response)
     print("Code retrieved successfully: %s" % code)
     # encode data
     encoded64 = encode_data(client_id=client_id, client_secret=client_secret)
     token = get_access_token(code=code,
                      redirect_uri=redirect_uri,
                      encoded64=encoded64
                      )
     return token


def refresh_access_token(old_token, encoded64):
     refresh_url = "https://accounts.spotify.com/api/token"

     params = {"grant_type": "refresh_token",
               "refresh_token": old_token}

     headers = {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": "Basic " + encoded64
          }
     
     response = requests.post(refresh_url, params=params, headers=headers)

     if response.status_code == 200:
          print("Successfully retrieved token")
          token_json = response.json()
          new_token = token_json['access_token']
          return new_token
     else:
          print("Something went wrong! Response status code: %s" % response.status_code)

def refresh_token():
     client_id = input("Please paste here your client id: ")
     client_secret = input("Please paste here your client secret: ")
     old_token = input("Please paste here your old token: ")

     encoded64 = encode_data(client_id=client_id, client_secret=client_secret)
     new_token = refresh_access_token(old_token=old_token,
                                      encoded64=encoded64)

if __name__=="__main__":
     import sys

     arguments = sys.argv

     if "GET" in arguments:
          token = get_token()
          print(token)
     
     elif "REFRESH" in arguments:
          new_token = refresh_token()
          print(new_token)