import sys
from tkinter.constants import NW

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
