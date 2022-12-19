import os
import random
import webbrowser

import playerList
import requests
import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer
import urllib

from io import BytesIO
from PIL import Image


def randomImage():
    folder = r"/media/pi/Volume"
    image = None
    file = None

    while file is None:
        temp = random.choice(os.listdir(folder))
        if not (temp == "$RECYCLE.BIN" or temp == "System Volume Information"):
            file = f'{folder}\\{temp}'

    while image is None:
        try:
            image = Image.open(file)
            print(f'{file}')
            imageViewer.showPIL(image, 5000)
        except PermissionError as e:
            file = f'{file}/{random.choice(os.listdir(file))}'
        except IsADirectoryError as e:
            file = f'{file}/{random.choice(os.listdir(file))}'
        except OSError as e:
            return


def randomGif():
    url = "https://api.giphy.com/v1/gifs/random?api_key=1Q55dtdlmXmoMseH70jeOHIv29sGrPwa"
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

random.shuffle(playerList.list)

while True:
    for element in playerList.list:
        youtubePlayer.openYoutube(element)
