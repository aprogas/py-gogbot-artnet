#!/usr/bin/python

# 2013-11-08 Aprogas
# Encodes the last octet of each IP-address into a set of colored stripes.
# There are 3 stripes with 4 possible colors and a small white stripe to
# indicate the most significant side. Each color corresponds to a number, this
# is basically just base-4 math. Black is 0, red is 1, green is 2, blue is 3.
#
# Tips:
#  - let the DHCP-server start numbering lights at .1 and put the router at
#    .254; low numbers are easier to calculate from the head
#  - set the DHCP-server leasetime to a week or longer so addresses don't
#    change during the festival
#
# Cheatsheet:
# +--------+-------+-------+-------+-------+
# | Stripe | Black | Red   | Green | Blue  |
# +--------+-------+-------+-------+-------+
# | 1      |     0 |     1 |     2 |     3 |
# | 2      |     0 |     4 |     8 |    12 |
# | 3      |     0 |    16 |    32 |    48 |
# | white  | N/A   | N/A   | N/A   | N/A   |
# +--------+-------+-------+-------+-------+
#
# TODO: Change back to 4 stripes to allow 256 values, instead of just 64, using
#       3 stripes was a brainfart (4**3 != 256)

import argparse
import socket
import time

from artnet import buildPacket

DEBUG = False
UDP_PORT = 6454
COLORS = ((0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)  # Allow broadcast

while (True):
    # Loop through all possible addresses
    for octet in xrange(1,256):
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
            # Fill a stripe with the right color
            for i in xrange(42):
                data.append(color)
        # Make a white stripe as order marker
        for i in xrange(24):
            data.append((255, 255, 255))
        sock.sendto(buildPacket(0, data), (addr, UDP_PORT))
        # Run slower in debug-mode
        time.sleep(0.1 + DEBUG)

sock.close()
