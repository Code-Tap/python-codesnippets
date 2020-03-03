#! /usr/bin/env python
""" Programme created by Leigh Wilson 3/2015
A slightly more complicated calculator that works out the area of
a triangle using the base x height devided by 2 method.
This version is set within a (while) loop using definitions (def)
and also gives the workings out for the user """

while True:
	def triangle():
		print "\nThis programme calculates the area of a triangle"
		base = raw_input("Enter base value: ")
		base2 = float(base)
		height = raw_input("Enter height value: ")
		height2 = float(height)
		area = base2 * height2 / 2
		print "The working out is, %d x %d / 2" % (base2, height2)
		print "Base x height =", base2 * height2
		print "Once devided by 2 the area of your triangle is ",area

	triangle()

# Slightly more complicated version that will work with decimals,
# and will also loop over and over to allow for repeated use untill
# the user decides to quit.

# This version has no Error Checking so it will fail if the user does
# not enter a value or enters a string.
