import discogs_client
d = discogs_client.Client('Pybay/0.1')
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

# TOKEN = os.environ['TOKEN']
USERNAME = os.environ['USERNAME']
DISCOGS_PAGE_NUMBER = 1

import requests
response = requests.get(f"https://api.discogs.com/users/{USERNAME}/wants?page={DISCOGS_PAGE_NUMBER}&per_page=50").json()

new_dict = {}
for key, value in response.items():
    if key == "wants":
        new_dict = value

want_list = []

for release in new_dict:
    title = release["basic_information"]["title"]
    artist = release["basic_information"]["artists"][0]["name"]
    want_list.append(artist + " " + title)

print(want_list)

with open("wantlist.json", 'w') as f:
    json.dump(want_list, f, indent=2) 