import time
import random
import os
import playerList
from pynput.keyboard import Key, Controller


def openYoutube(i):
    keyboard = Controller()

    element = playerList.list[random.randrange(len(playerList.list))]

    print(element.name)

    if element.type == 1:
        str = f'{element.link}&t={element.length - random.randrange(30, element.length)}s'
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

    time.sleep(random.uniform(1, 3))

    keyboard.press(Key.ctrl_l)
    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)
