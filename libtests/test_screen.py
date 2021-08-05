#!/usr/bin/env python3

# Run with:
# sudo service icopy stop
# DISPLAY=:0 sudo xinit /usr/bin/python3 test_screen.py

import time
import platform
import tkinter as tk
from PIL import ImageTk, Image

import keymap
import hmi_driver as hmi

class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        self.label = tk.Label(parent, text="Hello World!", font=("mononoki", 10 * fontfactor))
        self.label.pack(padx=20, pady=20)

        self.img = ImageTk.PhotoImage(Image.open("test_screen.jpg").resize((160, 160)))

#        self.label2 = tk.Label(parent, image=self.img)
#        self.label2.pack(padx=20, pady=0)

        self.canvas = tk.Canvas(parent, width = 240, height = 240)
        self.canvas.pack()
        self.canvas.create_image(40, 0, anchor=tk.NW, image=self.img)

def keydbg(event):
    print("MyDBG:", event)

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("240x240")
    root.config(cursor="none")
#    root.option_add("*Font", "mononoki")
    root.bind("<Key>", keymap.key.onKey)
    # Maybe just an effect of HiDPI on host?
    global fontfactor
    if platform.processor() == 'armv7l':
        fontfactor = 2
    else:
        fontfactor = 1

    main = HelloWorld(root)
    main.pack(fill="both", expand=True)
    keymap.key.bind(keydbg)
    if platform.processor() == 'armv7l':
        hmi.starthmi()
        print("STM32 ID:", hmi.readstid().decode('UTF8'))

    # Last:
    root.mainloop()
