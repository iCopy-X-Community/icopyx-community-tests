#!/usr/bin/env python3

# sudo service icopy stop
# DISPLAY=:0 sudo python3 xbubble_bindkeys.py

import platform
if platform.processor() != 'armv7l':
    raise Exception("Cannot run on host")

import xdo
from xdo import Xdo

import keymap
import hmi_driver as hmi

def keydbg(event):
    print("MyDBG:", event)
    if event == 'UP':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"Up", delay=50000)
    if event == 'DOWN':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"Down", delay=50000)
    if event == 'LEFT':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"Left", delay=250000)
    if event == 'RIGHT':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"Right", delay=250000)
    if event == 'M2':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"p")
    if event == 'OK':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"Return")
    if event == 'POWER':
        x.send_keysequence_window(xdo.CURRENTWINDOW, b"q")

x=Xdo()
keymap.key.bind(keydbg)

hmi.starthmi()
