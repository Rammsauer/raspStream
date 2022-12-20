import sys
import random
import pyperclip
import os
import time

from pynput.keyboard import Key, Controller as kController
from PIL import Image, ImageTk

if sys.version_info[0] == 2:
    import Tkinter

    tkinter = Tkinter
else:
    import tkinter


def showPIL(pilImage, duration=1000):
    root = tkinter.Tk()

    # Escape action
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()

    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.pack()
    canvas.configure(background='black')

    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w / imgWidth, h / imgHeight)
        imgWidth = int(imgWidth * ratio)
        imgHeight = int(imgHeight * ratio)
        pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(pilImage)

    try:
        canvas.create_image(w / 2, h / 2, image=image)
        root.after(duration, lambda: (root.destroy()))

        root.mainloop()
    except OSError as e:
        return


def randomImage():
    folder = r"D:/Hi Res"
    image = None
    file = None

    while file is None:
        temp = random.choice(os.listdir(folder))
        if not (temp == "$RECYCLE.BIN" or temp == "System Volume Information"):
            file = f'{folder}/{temp}'

    while image is None:
        try:
            image = Image.open(file)
            pyperclip.copy(f'file:///{file}')
            print(f'{file}')
            pressKeys()
        except PermissionError as e:
            file = f'{file}/{random.choice(os.listdir(file))}'
        except IsADirectoryError as e:
            file = f'{file}/{random.choice(os.listdir(file))}'
        except OSError as e:
            return


# Bad practice fix soon
def pressKeys():
    keyboard = kController()

    keyboard.press(Key.alt_l)
    keyboard.press("d")

    time.sleep(0.5)

    keyboard.release(Key.alt_l)
    keyboard.release("d")

    keyboard.press(Key.ctrl_l)
    keyboard.press("l")

    time.sleep(0.5)

    keyboard.release(Key.ctrl_l)
    keyboard.release("l")

    keyboard.press(Key.ctrl_l)
    keyboard.press("v")

    # time.sleep(0.5)

    keyboard.release(Key.ctrl_l)
    keyboard.release("v")

    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
