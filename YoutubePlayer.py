import webbrowser
import time
import random
from pynput.keyboard import Key, Controller


class youtubeLink:
    def __init__(self, link, type, name):
        self.link = link
        self.type = type
        self.name = name


list = [
    youtubeLink("https://www.youtube.com/watch?v=QOjmvL3e7Lc", 0, "Tokyo Livecam"),
    youtubeLink("https://www.youtube.com/watch?v=-HAi_5IIAYg", 0, "Deerfield Beachcam"),
    youtubeLink("https://www.youtube.com/watch?v=seEkN2AFhBw", 0, "Harbour Village Bonaire Coral Reef"),
    youtubeLink("https://www.youtube.com/watch?v=odVgCqN6FXM", 0, "Utopia Village Reef Wall Camera"),
    youtubeLink("https://www.youtube.com/watch?v=ydYDqZQpim8", 0, "Namibia: Live stream in the Namib Desert"),
    youtubeLink("https://www.youtube.com/watch?v=JJqXeRFsLjE", 0, "KC Zoo Penguin Cam"),
    youtubeLink("https://www.youtube.com/watch?v=y1QoP1AgAlY", 0, "Raccoon Cam \"Living Room\""),
    youtubeLink("https://www.youtube.com/watch?v=N1QWE0eQDVI", 0, "LIVE Barn Owl Florida"),
    youtubeLink("https://www.youtube.com/watch?v=JnJhFYhIjFs", 0, "Port of Helsinki - West harbour - north cam"),
    youtubeLink("https://www.youtube.com/watch?v=m9ZzkweZKcM", 0, "Wetter-Panorama – 24/7 LIVE Stream Webcams Österreich"),
    youtubeLink("https://www.youtube.com/watch?v=JQnxefImhu8", 0, "Monterey Bay Aquarium"),
    youtubeLink("https://www.youtube.com/watch?v=RQA5RcIZlAM", 0, "Tokyo Shinjuku Live Cam"),
    youtubeLink("https://www.youtube.com/watch?v=qHJMkze8lPg", 0, "東京駅丸の内口　ライブカメラ"),
    youtubeLink("https://www.youtube.com/watch?v=emI8r2dfk6g", 0, "Main Street Livecam, Canmore, Alberta "),
    youtubeLink("https://www.youtube.com/watch?v=B0YjuKbVZ5w", 0, "Grand Avenue Bridge in Glenwood Springs Live Camera"),
    youtubeLink("https://www.youtube.com/watch?v=1EiC9bvVGnk", 0, "Jackson Hole Wyoming USA Town Square Live Cam - SeeJH.com"),
    youtubeLink("https://www.youtube.com/watch?v=V00D4K9OshI", 0, "LONDON BUS RIDES ✨ DIGEST 🔴 LIVE CHAT 💫"),
    youtubeLink("https://www.youtube.com/watch?v=FKLlUa23eCY", 0, "Berlin Bus Rides 🔴 Live Chat"),
    youtubeLink("https://www.youtube.com/watch?v=NKzejBusnE8", 0, "Views of Three Sisters from A Bear & Bison Inn"),
]


def openYoutube(i):
    keyboard = Controller()

    webbrowser.open(list[random.randrange(len(list))].link)

    time.sleep(15)

    if i > 1:
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.alt)
        keyboard.press(Key.esc)

        keyboard.release(Key.esc)
        keyboard.release(Key.alt)
        keyboard.release(Key.ctrl_l)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    keyboard.press('f')
    keyboard.release('f')

    time.sleep(30)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    time.sleep(random.uniform(1,3))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)