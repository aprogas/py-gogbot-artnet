#!/usr/bin/python

# 2013-09-02 Aprogas

import socket
import time

from artnet import buildPacket
from patterns import PolicePattern

UDP_PORT = 6454
TARGETS = {
	"10.0.0.10": PolicePattern(),
	"10.0.0.11": PolicePattern(backwards=True),
	"10.0.0.14": PolicePattern(backwards=True),
	"10.0.0.15": PolicePattern(),
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while (True):
	for t in TARGETS:
		pattern = TARGETS[t]
		data = pattern.generate()
		sock.sendto(buildPacket(0, data), (t, UDP_PORT))
	time.sleep(0.08)	

sock.close()
