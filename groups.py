# imports
import requests
import urllib, base64
import yaml
import json

# open config file
with open('config.yaml', 'r') as f:
    doc = yaml.safe_load(f)
KEY = doc['key']

# create group id
group_id = 'house'
params = urllib.parse.urlencode({'personGroupId': group_id})
body = '{"name": "House"}'
headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': KEY}
# request
response = requests.put(doc['url-group'], params=params, headers=headers, data=body)
data = response.json()
print(data)
