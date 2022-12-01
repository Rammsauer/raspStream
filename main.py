import os
import random
import time

import playerList
import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer

from PIL import Image

indexYoutube = 0


def randomImage():
    folder = r"D:\\40k art collection"
    image = None
    file = None

    while file is None:
        temp = random.choice(os.listdir(folder))
        if temp == "$RECYCLE.BIN" or temp == "System Volume Information":
            file = None
        else:
            file = f'{folder}\\{temp}'

    while image is None:
        try:
            image = Image.open(file)
        except PermissionError as e:
            file = f'{file}\\{random.choice(os.listdir(file))}'

    print(f'{file} | ')
    imageViewer.showPIL(image, 5000)


def randomVideo(i):
    random.shuffle(playerList.list)

    element = playerList.list[i]

    youtubePlayer.openYoutube(element, i)


while True:
    randomImage()

# while True:
#    randomVideo(indexYoutube)
#    indexYoutube = + 1
