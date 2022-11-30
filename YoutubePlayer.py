import time
import random
import os
from pynput.keyboard import Key, Controller


class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length


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
    youtubeLink("https://www.youtube.com/watch?v=zomZywCAPTA", 1, "4K CABVIEW Bar - Bijelo Polje -102 tunnels -96 bridges -1029m", 12377),
    youtubeLink("https://www.youtube.com/watch?v=oN8q7p57nZw", 1, "ASMR Night Truck Driving 1.5 Hours", 6119),
    youtubeLink("https://www.youtube.com/watch?v=V03JLp2rdKc", 1, "Walking New York City on a Spring-like Day", 2354),
    youtubeLink("https://www.youtube.com/watch?v=kasGRkfkiPM", 1, "Bob Ross - Mountain Summit (Season 13 Episode 10)", 1666),
    youtubeLink("https://www.youtube.com/watch?v=pw5ETGiiBRg", 1, "Bob Ross - Valley View (Season 21 Episode 1)", 1652),
    youtubeLink("https://www.youtube.com/watch?v=KYlM2zJnNWY", 1, "Bob Ross - Cabin in the Hollow (Season 31 Episode 5)", 1519),
    youtubeLink("https://www.youtube.com/watch?v=mT0RNrTDHkI", 1, "Bob Ross - One Hour Special - The Grandeur of Summer", 3582)
]


def openYoutube(i):
    keyboard = Controller()

    element = list[random.randrange(len(list))]

    if element.type == 1:
        str = f'{element.link}&t={element.length - random.randrange(30, element.length)}s'
        print(str)
        os.startfile(str)
    else:
        os.startfile(element.link)

    time.sleep(10)

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

    time.sleep(10)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    time.sleep(random.uniform(1,3))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)