#!/usr/bin/env python

import subprocess
import optparse
import re

# Class creates all arguements (interface & MacID)
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface", help="Interface to change the mac id")
    parser.add_option("-m","--mac-id", dest = "new_mac", help="Updated MacID")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("*[-] Please enter a valid network interface name, use --help for more info")
    elif not options.new_mac:
        parser.error("*[-] Please enter a valid mac address, use --help for more info")
    return options

# Class defines steps to change mac address
def change_mac(interface,new_mac):
    print("[+]. Changing mac address for "+interface+" to this value: "+new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Class makes sure that the current MacID is displayed, regex in use
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    filtered_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if filtered_mac:
        return filtered_mac.group(0)
    else:
        print("[-] Sorry mac address not found.")

options = get_arguments()

current_mac = get_current_mac(options.interface)  # here the current_mac variables value is old MacID
print("CURRENT MAC --> " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)  # here the current_mac variables value is the updated MacID
if current_mac == options.new_mac:
    print("[.] MAC Address was changed sucessfully to -->> " + current_mac)
else:
    print("[.] Changing MAC Address failed :( ")
