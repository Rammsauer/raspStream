import random
import webbrowser

import Constants
import playerList
import requests
import YoutubePlayer as youtubePlayer
import urllib

from io import BytesIO
from PIL import Image


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

while True:
    for element in playerList.videoList:
        youtubePlayer.openYoutube(element)



'''
not working build in later
while True:
    print(".", end='\r', flush=True)
    time.sleep(.5)
    print("..", end='\r', flush=True)
    time.sleep(.5)
    print("...", end='\r', flush=True)
    time.sleep(.5)
    print("", end='\r', flush=True)
    time.sleep(.5)
'''