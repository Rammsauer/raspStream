import time
import random
import webbrowser
from pynput.keyboard import Key, Controller as kController
from pynput.mouse import Listener, Button, Controller as mController


def openYoutube(element, i):
    keyboard = kController()
    mouse = mController()

    print(element.name)
    point = 0

    if element.type == 1:
        point = element.length - random.randrange(1, element.length)
        str = f'{element.link.replace("/wa", "/tv#/")}&t={point}s'
        webbrowser.open(str)
    else:
        webbrowser.open(element.link.replace("/wa", "/tv#/"))

    time.sleep(10)

    mouse.click(Button.left)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    if element.type == 1:
        if point < 1200:
            time.sleep(random.uniform(1, (element.length - point)))
        else:
            time.sleep(random.uniform(660, 1200))
    else:
        time.sleep(random.uniform(660, 1200))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)
