from scapy.all import *
import requests

def display(pkt):
  if DHCP in pkt and pkt.src == "[MAC ADDRESS]":
    print("Got button press")
    requests.post("https://maker.ifttt.com/trigger/[EVENT]/with/key/[KEY]")

sniff(prn=display, filter="udp", store=0)
