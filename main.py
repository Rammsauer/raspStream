import os
import random
import time

import playerList
import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer

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
        except PermissionError as e:
            file = f'{file}\\{random.choice(os.listdir(file))}'

    print(f'{file}')
    imageViewer.showPIL(image, 5000)


# while True:
#    randomImage()


random.shuffle(playerList.list)

while True:
    for element in playerList.list:
        youtubePlayer.openYoutube(element)
