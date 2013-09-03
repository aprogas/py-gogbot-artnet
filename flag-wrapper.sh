#!/bin/sh

# 2013-09-03 Aprogas

# Please keep sorted by English names
case "$1" in
	colombia)
		# Yellow(double) Blue Red
		./flag.py -c 255 255 0 -c 255 255 0 -c 0 0 255 -c 255 0 0
		;;
	enschede)
		# White Red White
		./flag.py -c 255 255 255 -c 255 0 0 -c 255 255 255
		;;
	germany|duitsland)
		# Black(off) Red Yellow
		./flag.py -c 0 0 0 -c 255 0 0 -c 255 255 0
		;;
	indonesia|indonesie)
		# Red White
		./flag.py -c 255 0 0 -c 255 255 255
		;;
	netherlands|nederland)
		# Red White Blue
		./flag.py -c 255 0 0 -c 255 255 255 -c 0 0 255
		;;
	poland|polen)
		# White Red
		./flag.py -c 255 255 255 -c 255 0 0
		;;
	prinsenvlag)
		# Oranje Blanje Blue
		./flag.py -c 255 153 0 -c 255 255 255 -c 13 71 255
		;;
	russia|rusland)
		# White Blue Red
		./flag.py -c 255 255 255 -c 0 0 255 -c 255 0 0
		;;
	ukraine)
		# Lightblue Yellow
		./flag.py -c 0 96 192 -c 255 255 0
		;;
	*|blackout|zwart)
		./flag.py -c 0 0 0
		;;
esac
