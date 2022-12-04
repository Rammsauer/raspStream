import time
import random
import webbrowser
import pyautogui
from pynput.keyboard import Key, Controller as kController
from pynput.mouse import Listener, Button, Controller as mController


def openYoutube(element):
    keyboard = kController()
    mouse = mController()

    imageLogIn = None
    imageNotAv = None
    point = (element.length - random.randrange(1, element.length)) if element.type == 1 else 1
    sleep = random.uniform(60, (element.length - point)) if element.type == 1 and (element.length - point) < 1200 else random.uniform(660, 1200)

    print(f'{element.link.replace("https://www.youtube.com/watch?v=", "")} | {int(sleep)}s | {element.name} ')

    if element.type == 1:
        str = f'{element.link.replace("/wa", "/tv#/")}&t={point}s'
        webbrowser.open(str)
    else:
        webbrowser.open(element.link.replace("/wa", "/tv#/"))

    while imageLogIn is None:
        try:
            location1 = pyautogui.locateCenterOnScreen('img1.png')
            location2 = pyautogui.locateCenterOnScreen('img3.png')
            if location1 or location2:
                imageLogIn = True
        except Exception as e:
            imageLogIn = None

    time.sleep(5)

    mouse.click(Button.left)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(15)

    location = pyautogui.locateOnScreen('img2.png')
    if location: imageNotAv = True

    if not imageNotAv: time.sleep(sleep - 15)
    else: print("Stream aktuell nicht verfügbar")

    keyboard.press(Key.ctrl_l)

    time.sleep(5)

    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)

    time.sleep(5)
