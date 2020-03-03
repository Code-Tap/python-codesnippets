#! /usr/bin/env python
""" Programme created by Leigh Wilson 3/2015
An even more complicated calculator that not only works out the area of
a triangle using the base x height devided by 2 method.
It also has Error Checking on the user input to make sure the user is 
entering a number and not a letter (isdigit()) and forces the programme
to run again if an error is found.
I have also added a continuation prompt to allow the programme to exit 
cleanly when the user is ready.
This version is set within a (while) loop using definitions (def)
and also gives the workings out for the user """

while True:
	def triangle():
		print "\nThis programme calculates the area of a triangle"
		base = raw_input("Enter base value: ")
		height = raw_input("Enter height value: ")
		if base.isdigit() and height.isdigit():
			base2 = float(base)
			height2 = float(height)
			area = base2 * height2 / 2
		else:
			print "\nPlease enter numbers and not letters"
			triangle()
		print "The working out is, %d x %d / 2" % (base2, height2)
		print "Base x height =", base2 * height2
		print "Once devided by 2 the area of your triangle is ",area
	re_run = raw_input("\nDo you wish to continue? Y/N ")
	re_run.lower()
	if re_run == "y" or re_run == "yes":
		triangle()
	else:
		exit()

triangle()

# Even more complicated version that will work with decimals, letters
# and will also loop over and over to allow for repeated use untill
# the user decides to quit.

# This version has Error Checking so it should be fairly robust. 
#Remember in python, indentation is everything... as are colons! :
