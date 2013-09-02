#!/usr/bin/python

import random

class PolicePattern:
	# Rotating blue line with fading trail
	def __init__(self, backwards=False):
		self.backwards = backwards
		self.pos = 0

	def generate(self):
		data = []
		if self.backwards:
			leds = xrange(150, 0, -1)
		else:
			leds = xrange(0, 150, 1)
		for i in leds:
			place = (i % 7) + self.pos
			if (place >= 7):
				place -= 7
			distance = abs(3 - place)
			val = 2 - distance
			if (val < 0):
				val = 0
			val /= 2.0
			r = 0
			g = 0
			b = int(val * 255.0)
			data.append((r, g, b))
	
		self.pos += 1
		if (self.pos >= 7):
			self.pos = 0
	
		return data

class BarberpolePattern:
	# Rotating red/white stripes
	def __init__(self, backwards=False):
		self.backwards = backwards
		self.pos = 0

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
			
class RainPattern:
	# Falling white/blue-ish drops
	def __init__(self):
		# Init empty data list
		self.data = []
		for i in xrange(150):
			self.data.insert(0, (0, 0, 0))  # black/off

	def generate(self):
		for i in xrange(7):
			self.data.pop()
			if (not random.randrange(25)):
				self.data.insert(0, (150, 150, 255))  # white/blue-ish
			else:
				self.data.insert(0, (0, 0, 0))  # black/off

		return self.data
