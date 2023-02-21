import json
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
    playerList.rawList = youtubePlayer.getPlayList()

    youtubePlayer.fetchData()

    while True:
        for element in playerList.videoList:
            youtubePlayer.openYoutube(element)


def updateList():
    jsonList = []

    for element in playerList.rawPlaylist:
        jsonList.append({
            "id": element.id,
            "name": element.name
        })

    file = open("list.json", "w")
    json.dump(jsonList, file, indent=2)
    file.close()


updateList()
playVideos()
