import os
import random
import time

import ImageViewer as imageViewer
import YoutubePlayer as youtubePlayer

from PIL import Image


def randomImage():
    folder = r"C:\Users\l.rudolph\Pictures\Screenshots"

    a = random.choice(os.listdir(folder))
    print(a)

    file = folder + '\\' + a
    img = Image.open(file)
    imageViewer.showPIL(img)


# randomImage()

for i in range(1, 15):
    youtubePlayer.openYoutube(i)
