#!/usr/bin/env python

from scapy.all import ARP,Ether,srp
import argparse

# Class to create ip arguements (Pick Subnet-mask)
def get_arguements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest = "target", help="Enter a valid network target whose mac is to be scanned.")
    options = parser.parse_args()
    return options
    if not options.target:
        parser.error("[-] Please enter a valid target network, use --help for more info.")

    
def scan(ip):
    arp_request           = ARP(pdst=ip) 
    broadcast             = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list         = srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    clients_list          = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\t  MAC Address\n------------------------------------------ ")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguements()
scan_result = scan(options.target)
print_result(scan_result)
