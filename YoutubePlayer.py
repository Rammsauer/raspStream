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
        str = f'{element.link}&t={point}s'
        webbrowser.open(str)
        #os.startfile(str)
    else:
        webbrowser.open(element.link)
        #os.startfile(element.link, 'open')

    time.sleep(10)

    if i > 0:
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

    if element.type == 1:
        print(random.uniform(60, element.length - point))
        time.sleep(random.uniform(300, 600))#element.length - point))
    else:
        time.sleep(random.uniform(300, 600))


    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    time.sleep(random.uniform(1, 3))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)
