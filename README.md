# Overview

Python script which plays random videos from a pool in the browser. 
The script was written for a Raspberry Pi 3 Model B, with the additional browser addons it is platform independent.

For the Raspberry Pi it is recommended to set the screen resolution to 1280x720 and the GPU memory to 128 MB in the settings. 
This can be achieved in the console with the command. <br>
``
sudo raspi-config
``


### Chromium Add-ons

- [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=de)
- [Fullscreen Anything](https://chrome.google.com/webstore/detail/fullscreen-anything/olcfgpmjldkkjdclidhcbonieibfhhdh?hl=de)
- [h264ify](https://chrome.google.com/webstore/detail/h264ify/aleakchihdccplidncghkekgioiakgal?hl=de)

### Extra PIP installations
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
### Running the Script
``
python3 main.py
``

### Videopool
The video pool with its playlists is located in the following [file](https://github.com/Rammsauer/raspStream/blob/master/playerList.py).

The playlist urls are currently still hardcoded, since according to the [YouTube API Docs](https://developers.google.com/youtube/v3/docs) it is not yet possible to get saved playlists from your channel. 
Single videos can be saved under the playlist "[Livingroom Stream](https://www.youtube.com/playlist?list=PLHNwwBUMYsHYK4Klp5_YsHbPMecplf_-7)", which is also stored in the Videopool file.