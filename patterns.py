#!/usr/bin/python

# 2013-09-02 Aprogas

import math

class PolicePattern:
	def __init__(self, backwards=False):
		self.backwards = backwards
		self.pos = 0.0

	def generate(self):
		data = []
		if self.backwards:
			leds = xrange(150, 0, -1)
		else:
			leds = xrange(0, 150, 1)
		for i in leds:
			place = (i % 7) + self.pos
			if (place >= 7.0):
				place -= 7.0
			distance = math.fabs(3.0 - place)
			val = 2.0 - distance
			if (val < 0.0):
				val = 0.0
			val /= 2.0
			r = 0
			g = 0
			b = int(val * 255.0)
			data.append((r, g, b))
	
		self.pos += 0.2
		if (self.pos >= 7.0):
			self.pos = 0.0
	
		return data
