#!/usr/bin/python

import random

class PolicePattern:
	# Rotating line with fading trail, default color blue
	def __init__(self, backwards=False, color=(0, 0, 255)):
		self.backwards = backwards
		self.color = color
		self.pos = 0

	def generate(self):
		data = []
		if self.backwards:
			leds = xrange(150, 0, -1)
		else:
			leds = xrange(0, 150, 1)
		for i in leds:
			# Light one LED at full strength, its neighbors at half
			place = (i % 7) + self.pos
			if (place >= 7):
				place -= 7
			distance = abs(3 - place)
			# val becomes 0 0.5 or 1
			val = 2 - distance
			if (val < 0):
				val = 0
			val /= 2.0
			# Multiply RGB-values by val
			color = map(lambda x: int(x * val), self.color)
			data.append(color)

		self.pos += 1
		if (self.pos >= 7):
			self.pos = 0

		return data

class BarberpolePattern:
	# Rotating stripes of certain colors, default red/white
	def __init__(self, backwards=False, color1=(255, 0, 0), color2=(255, 255, 255)):
		self.backwards = backwards
		self.color1 = color1
		self.color2 = color2
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
				data.append(self.color1)
			else:
				data.append(self.color2)

		self.pos += 1
		if (self.pos >= 6):
			self.pos = 0

		return data

class RainPattern:
	# Falling drops, default color white/blue-ish
	def __init__(self, color=(150, 150, 255), chance=0.04):
		# Init empty data list
		self.color = color
		self.chance = chance
		self.data = []
		for i in xrange(150):
			self.data.insert(0, (0, 0, 0))  # black/off

	def generate(self):
		# Pop 7 times to move one line down
		for i in xrange(7):
			self.data.pop()
			if (random.random() < self.chance):  # random chance of raindrop
				self.data.insert(0, self.color)
			else:
				self.data.insert(0, (0, 0, 0))  # black/off

		return self.data

class ColorFadePattern:
	# Integral color shifting
	def __init__(self):
		self.phase = 0
		self.phasetable = [
			(255,   0,   0),
			(255,  64,   0),
			(255, 128,   0),
			(255, 192,   0),
			(255, 255,   0),
			(192, 255,   0),
			(128, 255,   0),
			( 64, 255,   0),
			(  0, 255,   0),
			(  0, 192,   0),
			(  0, 192,  64),
			(  0, 192, 128),
			(  0, 255, 192),
			(  0, 255, 255),
			(  0, 192, 255),
			(  0, 128, 255),
			(  0,   0, 255),
			( 64,   0, 255),
			(128,   0, 255),
			(192,   0, 255),
			(255,   0, 255),
			(255, 128, 255),
			(255, 255, 255),
			(255, 255, 128),
			(255, 128, 128),
			(255, 128,   0),
		]

	def generate(self):
		data = []
		for i in xrange(150):
			r, g, b = self.phasetable[self.phase]
			data.append((r, g, b))

		self.phase += 1
		if (self.phase >= len(self.phasetable)):
			self.phase = 0

		return data
