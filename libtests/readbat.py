#!/usr/bin/env python3

# sudo service icopy stop
# sudo python3 readbat.py

import platform
if platform.processor() != 'armv7l':
    raise Exception("Cannot run on host")

import serial
ser_instance = serial.Serial('/dev/ttyS0', 57600, timeout=None)
ser_instance.write(b"pctbat\r\n")
print(ser_instance.readline().decode('utf8'))
# flush OK
ser_instance.readline()
