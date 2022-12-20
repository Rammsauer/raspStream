import os
import random
import time
import webbrowser

import Constants
import playerList
import requests
import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer
import urllib
import pyperclip

from io import BytesIO
from PIL import Image
from pynput.keyboard import Key, Controller as kController


def randomGif():
    url = f'https://api.giphy.com/v1/gifs/random?api_key={Constants.giphyApiKey}'
    response = requests.get(url)
    id = response.json()['data']['id']
    gifUrl = f'https://i.giphy.com/media/{id}/giphy.gif'
    print(gifUrl)
    image = Image.open(BytesIO(urllib.request.urlopen(gifUrl).read()))
    webbrowser.open_new(gifUrl)


'''
while True:
    randomGif()
'''

youtubePlayer.fetchData()

random.shuffle(playerList.videoList)

print(playerList.videoList)
'''
while True:
    for element in playerList.list:
        youtubePlayer.openYoutube(element)
'''