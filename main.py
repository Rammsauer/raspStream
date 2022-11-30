import os
import random
import time
import playerList
import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer

from PIL import Image

indexYoutube = 0


def randomImage():
    folder = r"C:\Users\l.rudolph\Pictures\Screenshots"

    a = random.choice(os.listdir(folder))
    print(a)

    file = folder + '\\' + a
    img = Image.open(file)
    imageViewer.showPIL(img)


def randomVideo(i):
    random.shuffle(playerList.list)

    element = playerList.list[i]

    youtubePlayer.openYoutube(element, i)


for i in range(1, 15):
    randomVideo(indexYoutube)
    indexYoutube = + 1
