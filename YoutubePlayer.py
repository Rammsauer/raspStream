import os
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
    sleep = random.uniform(int((element.length - point) * 0.8),
                           int((element.length - point) * 0.9)) if element.type == 1 and (
            element.length - point) < 1200 else random.uniform(660, 1200)

    print(f'{"Livestream" if element.type == 0 else "Video"} | '
          f'{int(sleep)}s | '
          f'{id}&t={point}s | '
          f'{element.name.replace("|", ",")}')

    webbrowser.open(f'{element.link}&t={point}s' if element.type == 1 else element.link)

    refreshData()

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
          f'part=liveStreamingDetails,contentDetails,snippet&' \
          f'id={id}&' \
          f'key={Constants.youtubeApiKey}'

    try:
        item = requests.get(url).json().get("items")[0]

        name = item.get("snippet").get("title")
        type = 1 if item.get("contentDetails").get("duration") != "P0D" else 0
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


def getPlayList():
    print("Fetching playlist...")
    return requests.get(Constants.rawJsonPlaylist).json()


def fetchData():
    for element in playerList.rawList:
        print(f'Fetching \"{element.get("name")}\" please wait ... ', end="")
        fetchPlaylist(element)

    print('Shuffling list ...')
    shuffleList()

    #print(f'Distinct list, deleted {len(playerList.videoList) - len(list(set(playerList.videoList)))} items')
    #playerList.videoList = list(set(playerList.videoList))
    #print(f'Fetched {len(playerList.videoList)} items')


def fetchPlaylist(element):
    response = ""
    tempList = []

    while True:
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?' \
              f'part=contentDetails&' \
              f'playlistId={element.get("id")}&' \
              f'key={Constants.youtubeApiKey}&' \
              f'maxResults=50&' \
              f'pageToken={response.get("nextPageToken") if response != "" else ""}'

        response = requests.get(url).json()

        for elements in response.get("items"):
            tempList.append(elements.get("contentDetails").get("videoId"))

        if response.get("nextPageToken") is None:
            playerList.playListWithVideos.append(
                playerList.playList(
                    id=element.get("id"),
                    name=element.get("name"),
                    videoList=tempList
                )
            )
            print(f'fetched {len(tempList)} of {response.get("pageInfo").get("totalResults")} videos')
            break


def refreshData():
    end = time.time()

    # after 24 hours the list will be refreshed
    if end - playerList.timeStamp < 86400:
        return

    os.system("sudo apt clean")

    print(f'Refreshing Data ... ')

    playerList.videoList = []
    playerList.rawList = getPlayList()
    fetchData()
    playerList.timeStamp = time.time()


def shuffleList():
    isEmpty = False

    while not isEmpty:
        tempList = playerList.playListWithVideos

        random.shuffle(tempList)

        for i in range(-1, len(tempList) - 1):
            if i < len(tempList):
                element = tempList[i]

                videoId = random.choice(element.videoList)
                element.videoList.remove(videoId)

                playerList.videoList.append(videoId)

                if not element.videoList:
                    playerList.playListWithVideos.remove(element)

            if len(playerList.playListWithVideos) == 0:
                isEmpty = True
