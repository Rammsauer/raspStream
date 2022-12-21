# Overview

Python Script which plays random videos on Raspberry Pi 3 model B. <br>

## Chromium Add-ons

- [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=de)
- [Fullscreen Anything](https://chrome.google.com/webstore/detail/fullscreen-anything/olcfgpmjldkkjdclidhcbonieibfhhdh?hl=de)
- [h264ify](https://chrome.google.com/webstore/detail/h264ify/aleakchihdccplidncghkekgioiakgal?hl=de)

## PIP Add-ons
- pynput

``
python3 -m pip install pynput
``
- isodate

``
python3 -m pip install isodate
``
- tkinter

``
python3 -m pip install tkinter
``
## Running the Script
``
python3 main.py
``

## Videopool
The Pool of Videos can be found under [the following file](https://github.com/Rammsauer/raspStream/blob/master/playerList.py). 
There are currently hardcoded Playlisturls witch will be fetched at the beginning, because it is currently not possible to fetch saved playlist, according to [YouTube API Docs](https://developers.google.com/youtube/v3/docs).
