#!/usr/bin/python

# 2013-09-02 Aprogas

import argparse
import socket
import time

from artnet import buildPacket

from police_conf import TARGETS

UDP_PORT = 6454

parser = argparse.ArgumentParser(description="Rotating police light.")
parser.add_argument("-d", "--delay", nargs="?", default=0.08, type=float)
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
