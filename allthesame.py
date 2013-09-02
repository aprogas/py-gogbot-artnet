#!/usr/bin/python

# 2013-09-02 Aprogas

import argparse
import socket
import time

from artnet import buildPacket

UDP_PORT = 6454

parser = argparse.ArgumentParser(description="Send the same color to all LEDs.")
parser.add_argument("red"  , type=int, nargs='?', default=0)
parser.add_argument("green", type=int, nargs='?', default=0)
parser.add_argument("blue" , type=int, nargs='?', default=0)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
	data = []
	for i in xrange(150):
		data.append((args.red, args.green, args.blue))
	sock.sendto(buildPacket(0, data), ("10.0.0.255", UDP_PORT))
	time.sleep(1)	

sock.close()
