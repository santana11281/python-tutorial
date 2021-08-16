import json
import requests

url = 'https://torrent-app-v2.herokuapp.com/top-movies'

r = requests.get(url)
response = r.json()
print(json.dumps( response,indent=4))

numbers = 1
