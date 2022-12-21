import random
import time

import playerList
import YoutubePlayer as youtubePlayer
import ImageViewer
import subprocess

'''
while True:
    image = ImageViewer.randomImage()

while True:
    randomGif()
'''

playerList.timeStamp = time.time()

youtubePlayer.fetchData()

random.shuffle(playerList.videoList)

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