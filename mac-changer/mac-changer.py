#!/usr/bin/env python

# variables
#interfaces = "eth0"
#new_mac    = "11:22:33:44:bb:aa"

import subprocess
import optparse

parser     = optparse.OptionParser()
parser.add_option("-i","--interface", dest = "interface", help="Interface to change the mac id")
parser.add_option("-m","--mac-id", dest = "new_mac", help="Updated MacID")
(options, arguements) = parser.parse_args()

interface  = options.interface
new_mac    = options.new_mac

print("[+]. Changing mac address for "+interface+"to this value: "+new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
