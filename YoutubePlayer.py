import time
import random
import webbrowser
from pynput.keyboard import Key, Controller as kController


def openYoutube(element):
    keyboard = kController()

    point = (element.length - random.randrange(int(element.length/2), element.length)) if element.type == 1 else 1
    sleep = random.uniform(int((element.length-point)*0.8), (element.length - point)) if element.type == 1 and (element.length - point) < 1200 else random.uniform(660, 1200)

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

