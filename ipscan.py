#!/usr/bin/python3
import scapy.all as scapy
import socket

hostname = socket.gethostname()
ipadres2 = socket.gethostbyname(f"{hostname}.local")
print(f"Client IP address: {ipadres2}")
ipadres3 = str(ipadres2).split('.')
ipadres3[-1] = '0'
ipadres = ('.'.join(ipadres3))
NETWORK = f"{ipadres}/24"
print(NETWORK)
print("IPADRES" + " " * 13 + "MAC" + f"\n\n")
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for host in answered_list:
        ruimte = len(host[1].psrc)
        space = " " * (20 - ruimte)
        print(f"{host[1].psrc}{space}{host[1].src}")

scan(NETWORK)
