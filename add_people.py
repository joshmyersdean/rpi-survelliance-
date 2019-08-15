import urllib, base64, json
import requests
import sys
import os
import yaml


# open config file
with open('config.yaml', 'r') as f:
    doc = yaml.safe_load(f)

people = [doc['person1'], doc['person2']]
name_id = []
group_id = 'house'
KEY = doc['key']

def add():
    headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': KEY}
    params = urllib.parse.urlencode({'personGroupId': group_id})
    for person in people:
        body = "{'name': '"+person+"'}"
        response = requests.post(doc['url-group']+"/persons", params=params, headers=headers, data=body)
        data = json.loads(response.text) # turns response into index-able dictionary
        out = person+"'s ID: " +data['personId']
        print(out)
        name_id.append((person, data['personId']))
    return name_id

add()
