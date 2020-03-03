#!/usr/bin/env python3
#scrollPhat_pulse.py

from scrollphat import *
from time import sleep

def initialise():
    for x in range(11):
        for y in range(5):
            set_pixel(x, y, True)
    update()

def fadein():
    for i in range(0,255,5):
        set_brightness(i)
        sleep(.05)

def fadeout():
    for i in range(255,0,-5):
        set_brightness(i)
        sleep(.05)

if __name__ == "__main__":
    initialise()
    while True:
    try:
        fadein()
        fadeout()
    except OSError:
        pass
    except KeyboardInterrupt:
    clear()
    raise SystemExit
