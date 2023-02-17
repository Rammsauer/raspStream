import json
import random
import time
import playerList
import YoutubePlayer as youtubePlayer

'''
not working build in later

while True:
    image = ImageViewer.randomImage()

while True:
    randomGif()
    
while True:
    print(".", end='\r', flush=True)
    time.sleep(.5)
    print("..", end='\r', flush=True)
    time.sleep(.5)
    print("...", end='\r', flush=True)
    time.sleep(.5)
    print("", end='\r', flush=True)
    time.sleep(.5)

import pyautogui

while True:
    time.sleep(60)

    pyautogui.click()
'''


def playVideos():
    playerList.timeStamp = time.time()
    playerList.list = youtubePlayer.getPlayList()

    youtubePlayer.fetchData()

    random.shuffle(playerList.videoList)

    while True:
        for element in playerList.videoList:
            youtubePlayer.openYoutube(element)


def updateList():
    jsonList = []

    for element in playerList.playlist:
        jsonList.append({
            "id": element.id,
            "name": element.name
        })

    f = open("list.json", "w")
    f.write(json.dumps(jsonList))
    f.close()


playVideos()
