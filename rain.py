#!/usr/bin/python

# 2013-09-02 Aprogas

import socket
import time

from artnet import buildPacket

from rain_conf import TARGETS

UDP_PORT = 6454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
	for t in TARGETS:
		pattern = TARGETS[t]
		data = pattern.generate()
		sock.sendto(buildPacket(0, data), (t, UDP_PORT))
	time.sleep(0.20)	

sock.close()
