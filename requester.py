# Make requests

import requests
import json

with open('token.json') as json_file:
    token = json.load(json_file)

print(token['access_token'])

# url = ''

# headers = {'Authorization': f'Bearer: {token['access token']}'}

# response = requests.get