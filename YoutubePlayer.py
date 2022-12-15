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
    timeStamp = time.time()
    point = (element.length - random.randrange(int(element.length/2), element.length)) if element.type == 1 else 1
    sleep = random.uniform(int(element.length*0.8), (element.length - point)) if element.type == 1 and (element.length - point) < 1200 else random.uniform(660, 1200)

    print(f'{element.link.replace("https://www.youtube.com/watch?v=", "")} | {int(sleep)}s | {element.name} ')

    if element.type == 1:
        webbrowser.open(f'{element.link}&t={point}s')

    else:
        webbrowser.open(element.link)

    '''
    while imageLogIn is None:
        try:
            location1 = pyautogui.locateCenterOnScreen('img1.png')
            if time.time() - timeStamp > 90:
                keyboard.press(Key.ctrl_l)
                time.sleep(5)
                keyboard.press('w')

                keyboard.release('w')
                keyboard.release(Key.ctrl_l)

                return
            if location1:
                imageLogIn = True
        except Exception as e:
            imageLogIn = None
    
    time.sleep(2)

    mouse.click(Button.left)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    '''

    time.sleep(sleep)

    keyboard.press(Key.ctrl_l)

    time.sleep(5)

    keyboard.press('w')

    keyboard.release('w')
    keyboard.release(Key.ctrl_l)

