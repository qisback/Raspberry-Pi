#!/usr/bin/env python

import time
from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import blinkt

blinkt.set_clear_on_exit()

def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()

blinkt.set_brightness(0.1)

while True:
    cpu = psutil.cpu_percent(interval=0.1)
    v = cpu / 100.0
    # Debug prints
    print cpu
    print v
    if (cpu < 10):
            show_graph(v,0,255,0)    # Green
    elif (cpu > 11) and (cpu < 20):
            show_graph(v,56,255,0)
    elif(cpu > 21) and (cpu < 30): # Lime
            show_graph(v,113,255,0)
    elif (cpu > 31) and (cpu < 40):
            show_graph(v,170,255,0)
    elif (cpu > 41) and (cpu < 50): # Yellow
            show_graph(v,226,255,0)
    elif (cpu > 51) and (cpu < 60):
            show_graph(v,255,226,0)
    elif (cpu > 61) and (cpu < 70): # Orange
            show_graph(v,255,170,0)
    elif (cpu > 71) and (cpu < 80):
            show_graph(v,255,113,0)
    elif (cpu > 81) and (cpu < 90):
            show_graph(v,255,56,0)
    elif (cpu >91):
            show_graph(v,255,0,0)  # Red
    time.sleep(0.01)


