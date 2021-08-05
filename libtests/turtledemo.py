#!/usr/bin/env python3

# Can be run on host too

# iCopy-X: Run with
# sudo service icopy stop
# DISPLAY=:0 sudo xinit /usr/bin/python3 turtledemo.py

import time
import platform
import tkinter as tk
import turtle
from PIL import ImageTk, Image

import keymap
import hmi_driver as hmi

def keydbg(event):
    print("MyDBG:", event)
    if event == 'UP':
        pen.fd(10)
    if event == 'LEFT':
        pen.left(90/4)
    if event == 'RIGHT':
        pen.right(90/4)
    if event == 'M1':
        pen.clear()
    if event == 'M2':
        if pen.isdown():
            pen.up()
        else:
            pen.down()
    if event == 'POWER':
        pen.reset()


root = tk.Tk()
root.resizable(False, False)
root.geometry("240x240")
root.config(cursor="none")
root.option_add("*Font", "mononoki")

turtle_canvas = turtle.Canvas(root)
turtle_canvas.pack(expand=True)

pen = turtle.RawTurtle(turtle_canvas)

root.bind("<Key>", keymap.key.onKey)
keymap.key.bind(keydbg)

if platform.processor() == 'armv7l':
    hmi.starthmi()

# Last:
root.mainloop()
