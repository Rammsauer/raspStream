import time
import random
import webbrowser
import requests
from pynput.keyboard import Key, Controller as kController

import Constants
import playerList


def openYoutube(element):
    keyboard = kController()

    point = (element.length - random.randrange(int(element.length / 2), element.length)) if element.type == 1 else 1
    sleep = random.uniform(int((element.length - point) * 0.8), (element.length - point)) if element.type == 1 and (
            element.length - point) < 1200 else random.uniform(660, 1200)

    if not isVideoAvailable(element.link.replace("https://www.youtube.com/watch?v=", ""), element.type):
        print(
            f'{element.link.replace("https://www.youtube.com/watch?v=", "")} | Currently not available | {element.name}')
        return

    print(f'{element.link.replace("https://www.youtube.com/watch?v=", "")} | {int(sleep)}s | {element.name} ')

    if element.type == 1:
        webbrowser.open(f'{element.link}&t={point}s')
    else:
        webbrowser.open(element.link)

    time.sleep(sleep)

    keyboard.press(Key.ctrl_l)

    time.sleep(5)

    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)


def isVideoAvailable(id, type):
    url = f'https://www.googleapis.com/youtube/v3/videos?' \
          f'part=liveStreamingDetails&' \
          f'id={id}&' \
          f'key={Constants.youtubeApiKey}'

    response = requests.get(url).json()

    if len(response.get("items")) == 0:
        return False

    if type == 0 and response.get("items")[0].get("liveStreamingDetails").get("concurrentViewers") is None:
        return False

    return True


def fetchData():
    for element in playerList.playlist:
        print(f'Fetching \"{element.name}\" please wait ... ')
        fetchPlaylist(element)

    print("Distinct list ... ")
    playerList.videoList = list(set(playerList.videoList))


def fetchPlaylist(element):
    response = ""

    while True:
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?' \
              f'part=contentDetails&' \
              f'playlistId={element.id}&' \
              f'key={Constants.youtubeApiKey}&' \
              f'maxResults=50&' \
              f'pageToken={response.get("nextPageToken") if response != "" else ""}'

        response = requests.get(url).json()

        for elements in response.get("items"):
            playerList.videoList.append(elements.get("contentDetails").get("videoId"))

        if response.get("nextPageToken") is None:
            break
