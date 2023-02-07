# Import dependencies
import base64
import requests
import re
from utils import write_textfile

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

def get_access_token(code, redirect_uri, client_id, client_secret):
     # Get access token
     token_url = "https://accounts.spotify.com/api/token"

     # Encode client ID and client secret
     encoded64 = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

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
          print("Successfully called API endpoint. Writing token to file")
          token_json = response.json()
          token = token_json['access_token']
          write_textfile(token, "token.txt")
          print("Successfully written token to file")
     else:
          print("Something went wrong! Response status code: %s" % response.status_code)

if __name__=="__main__":
     client_id = input("Please paste here your client id: ")
     client_secret = input("Please paste here your client secret: ")
     redirect_uri = "https://jpn-top-100.com/callback"
     response_url = request_authorization(client_id=client_id,
                                          redirect_uri=redirect_uri)
     print("Please authorize app using the following link: %s" % response_url)
     redirect_response = input("Paste the URL you are being redirected to here: ")
     code = get_code(redirect_response=redirect_response)
     print("Code retrieved successfully: %s" % code)
     get_access_token(code=code,
                      redirect_uri=redirect_uri,
                      client_id=client_id,
                      client_secret=client_secret
     )