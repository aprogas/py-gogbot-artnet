#!/usr/bin/python

# 2013-09-02 Aprogas

import argparse
import socket
import time

from artnet import buildPacket

UDP_PORT = 6454

parser = argparse.ArgumentParser(description="Make one or more horizontal stripes of certain color.")
parser.add_argument("-c", "--color", action="append", nargs=3, type=int)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

if (not args.color):
	# Default to pink
	args.color = [[84, 37, 42]]
while (True):
	data = []
	stripes = len(args.color)
	stripeheight = 150 / stripes
	for stripe in xrange(stripes):
		for i in xrange(stripeheight):
			data.append(args.color[stripe])
	sock.sendto(buildPacket(0, data), ("10.0.0.255", UDP_PORT))
	time.sleep(1)

sock.close()
