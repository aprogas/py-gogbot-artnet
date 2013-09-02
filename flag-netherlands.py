#!/usr/bin/python

# 2013-09-02 Aprogas

import socket
import time

from artnet import buildPacket

UDP_PORT = 6454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
	data = []
	for i in xrange(50):
		data.append((255, 0, 0))  # Red
	for i in xrange(50, 100):
		data.append((255, 255, 255))  # White
	for i in xrange(100, 150):
		data.append((0, 0, 255))  # Blue
	sock.sendto(buildPacket(0, data), ("10.0.0.255", UDP_PORT))
	time.sleep(1)	

sock.close()
