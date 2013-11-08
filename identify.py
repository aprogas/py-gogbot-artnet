#!/usr/bin/python

# 2013-09-02 Aprogas

import argparse
import socket
import time

from artnet import buildPacket

DEBUG = False
UDP_PORT = 6454
# black is 0, red is 1, green is 2, blue is 3
COLORS = ((0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
    # Loop the range configured in the DHCP-server
    for octet in xrange(10,250):
        data = []
        addr = "192.168.42.{}".format(octet)
        if DEBUG:
            print "=== {} ===".format(addr)
        for stripe in xrange(3):
            # Convert the last octet to base-4 and pick the right digit
            pos = (octet >> 2*stripe) % 4
            color = COLORS[pos]
            if DEBUG:
                print "stripe {} | pos {}".format(stripe, pos)
            for i in xrange(42):
                data.append(color)
        # Make 10 LEDs white as order marker
        for i in xrange(24):
            data.append((255, 255, 255))
        sock.sendto(buildPacket(0, data), (addr, UDP_PORT))
        time.sleep(0.1 + DEBUG)

sock.close()
