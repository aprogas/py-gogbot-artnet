#!/usr/bin/python

import random
import socket
import time

from artnet import buildPacket
from patterns import BarberpolePattern

UDP_PORT = 6454
TARGETS = {
	"10.0.0.10": BarberpolePattern(),
	"10.0.0.11": BarberpolePattern(backwards=True),
	"10.0.0.14": BarberpolePattern(backwards=True),
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while (True):
	for t in TARGETS:
		pattern = TARGETS[t]
		data = pattern.generate()
		sock.sendto(buildPacket(0, data), (t, UDP_PORT))
	time.sleep(0.1)	

sock.close()
