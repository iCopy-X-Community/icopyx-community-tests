#!/usr/bin/env python3

import platform
from tkinter import colorchooser

if platform.processor() == 'armv7l':
    raise Exception("Cannot run on iCopy-X")

colorchooser.askcolor()
