#!/usr/bin/python

import math

class PolicePattern:
	# Rotating blue line with fading trail
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

class BarberpolePattern:
	# Rotating red/white stripes
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
			place = (i % 6) + self.pos
			if (place >= 6):
				place -= 6
			if (place < 3):
				data.append((255, 0, 0))  # red
			else:
				data.append((255, 255, 255))  # white
	
		self.pos += 1
		if (self.pos >= 6):
			self.pos = 0
	
		return data
			
