''' Imports '''
import urllib, http.client, base64
import requests
from PIL import Image, ImageDraw
import sys
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from io import BytesIO
import yaml

# open config file
with open('config.yaml', 'r') as f:
    doc = yaml.safe_load(f)
KEY = doc['key']
pic = '0.jpg'

def face_recognition():
    face_api_url = doc['url']
    image_url = '0.jpg'
    # headers for image request
    headers = {'Ocp-Apim-Subscription-Key': KEY,
                'Content-Type': 'application/octet-stream',
                }
    body = open('0.jpg', 'rb') # image to recognize
    # parameters, the last one is really cool
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    # request
    response = requests.post(face_api_url, params=params,
                             headers=headers, data=body)
    photo_data = response.json()

    # draw rectangle around the face of the photo you are recognizing
    def getRectangle(faceDictionary):
        rect = faceDictionary['faceRectangle']
        left = rect['left']
        top = rect['top']
        bottom = left + rect['height']
        right = top + rect['width']
        return ((left, top), (bottom, right))

    img = Image.open(pic) # open image system argument
    draw = ImageDraw.Draw(img)
    for face in photo_data: # for the faces identified
        draw.rectangle(getRectangle(face), outline='blue') # outline faces in blue due to coordinates in json
    img.show() # display drawn upon image

# main call 
if __name__ == '__main__':
    face_recognition()
