#!/usr/bin/env python

from scapy.all import ARP,Ether,srp
def scan(ip):
    arp_request           = ARP(pdst=ip) 
    broadcast             = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose = False)[0]

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\t  MAC Address\n------------------------------------------ ")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan('10.0.0.1/24')
print_result(scan_result)
