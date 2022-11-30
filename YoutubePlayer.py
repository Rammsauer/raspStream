import time
import random
import os
import webbrowser
from pynput.keyboard import Key, Controller


def openYoutube(element, i):
    keyboard = Controller()

    print(element.name)
    point = 0

    if element.type == 1:
        point = element.length - random.randrange(1, element.length)
        str = f'{element.link.replace("watch?v=", "tv#/")}&t={point}s'
        webbrowser.open(str)
    else:
        webbrowser.open(element.link.replace("watch?v=", "tv#/"))

    #time.sleep(35)

    #keyboard.press(Key.space)
    #keyboard.release(Key.space)

    #keyboard.press('f')
    #keyboard.release('f')

    if element.type == 1:
        if point < 1200:
            time.sleep(random.uniform(1, (element.length - point)))
        else:
            time.sleep(random.uniform(660, 1200))
    else:
        time.sleep(random.uniform(660, 1200))


    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    time.sleep(random.uniform(1, 3))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)
