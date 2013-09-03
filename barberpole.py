#!/usr/bin/python

# 2013-09-03 Aprogas

import argparse
import socket
import time

from artnet import buildPacket

from barberpole_conf import TARGETS

UDP_PORT = 6454

parser = argparse.ArgumentParser(description="Rotating barber's pole.")
parser.add_argument("-d", "--delay", nargs="?", default=0.1, type=float)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
	for t in TARGETS:
		pattern = TARGETS[t]
		data = pattern.generate()
		sock.sendto(buildPacket(0, data), (t, UDP_PORT))
	time.sleep(args.delay)

sock.close()
