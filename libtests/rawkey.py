#!/usr/bin/env python3

# Helper to get host keycodes and keysyms
# Run with:
# sudo service icopy stop
# DISPLAY=:0 sudo xinit /usr/bin/python3 rawkey.py
# or on host:
# python3 rawkey.py

import platform
import tkinter as tk

import keymap
import hmi_driver as hmi

def keydbg(event):
    if type(event) is tk.Event:
       label2.configure(text=("keycode=%i" % event.keycode))
       label3.configure(text=("keysym=%s" % event.keysym))
    else:
       label2.configure(text=("keycode=N/A"))
       label3.configure(text=("keysym=%s" % event))

root = tk.Tk()
root.resizable(False, False)
root.geometry("240x240")
root.config(cursor="none")
root.bind("<Key>", keymap.key.onKey)

# Maybe just an effect of HiDPI on host?
if platform.processor() == 'armv7l':
    fontfactor = 2
else:
    fontfactor = 1
label = tk.Label(root, text="Press any key", font=("mononoki", 10 * fontfactor))
label.pack(padx=20, pady=20)
label2 = tk.Label(root, text="keycode=", font=("mononoki", 10 * fontfactor))
label2.pack(padx=20, pady=20)
label3 = tk.Label(root, text="keysym=", font=("mononoki", 8 * fontfactor))
label3.pack(padx=20, pady=20)
keymap.key.HOST_MAP = {}
keymap.key.bind(keydbg)
if platform.processor() == 'armv7l':
    hmi.starthmi()
    print("STM32 ID:", hmi.readstid().decode('UTF8'))
# Last:
root.mainloop()
