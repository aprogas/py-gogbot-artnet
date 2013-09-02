#!/usr/bin/python

import random
import socket
import time

from artnet import buildPacket

from barberpole_conf import TARGETS

UDP_PORT = 6454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while (True):
	for t in TARGETS:
		pattern = TARGETS[t]
		data = pattern.generate()
		sock.sendto(buildPacket(0, data), (t, UDP_PORT))
	time.sleep(0.1)	

sock.close()
