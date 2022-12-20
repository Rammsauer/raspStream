import time
import random
import webbrowser

import isodate as isodate
import requests

from pynput.keyboard import Key, Controller as kController

import Constants
import playerList


def openYoutube(id):
    keyboard = kController()

    element = getElement(id)

    # Videos shorter than 5 minutes will not be played
    if element.type == 1 and element.length < 600:
        return

    point = (element.length - random.randrange(int(element.length / 2), element.length)) if element.type == 1 else 1
    sleep = random.uniform(int((element.length - point) * 0.8), (element.length - point)) if element.type == 1 and (
            element.length - point) < 1200 else random.uniform(660, 1200)

    print(f'{id}&t={point}s | {int(sleep)}s | {"Livestream" if element.type == 0 else "Video"} ')

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


def getElement(id):
    name, type, duration = getVideoInformation(id)

    return playerList.youtubeLink(
        link=f'https://www.youtube.com/watch?v={id}',
        type=type,
        name=name,
        length=duration
    )


def getVideoInformation(id):
    url = f'https://www.googleapis.com/youtube/v3/videos?' \
          f'part=liveStreamingDetails,contentDetails&' \
          f'id={id}&' \
          f'key={Constants.youtubeApiKey}'

    try:
        item = requests.get(url).json().get("items")[0]

        name = id
        type = 1 if item.get("liveStreamingDetails") is None else 0
        duration = isodate.parse_duration(item.get("contentDetails").get("duration")).seconds

        return name, type, duration
    except IndexError as e:
        return id, 1, 0


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
    print(f'Fetched {len(playerList.videoList)} items')


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
            print(f'Fetched {response.get("pageInfo").get("totalResults")} videos')
            break
