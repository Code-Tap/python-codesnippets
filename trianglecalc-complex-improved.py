#! /usr/bin/env python

#
#
#========= ( EXPLANATION OF FIRST LINE )=========#
#
#

'''
If you have several versions of Python installed, /usr/bin/env will 
ensure the interpreter used is the first one on your environment's 
$PATH. The alternative would be to hardcode something line 
#!/usr/bin/python or the like -- that's OK but less flexible.

In Unix / Linux, an executable file that's meant to be interpreted can 
indicate what interpreter to use by having a #! at the start of the 
first line, followed by the interpreter (and any flags it may need).

With other platforms like Windows, of course, this rule does not 
apply (but that "shebang line" does no harm, and will help if you ever 
copy that script to a platform with a Unix base, such as Linux or Mac.
'''

#
#
#========= ( LEIGH WILSON'S INTRODUCTION NOTES )=========#
#
#

''' 
Programme created by Leigh Wilson 3/2015
Final revision and most robust version of python calculator that not 
only works out the area of a triangle using the base x height devided 
by 2 method.
It also has an Error Checking function on the user input to make sure 
the user is entering a number and not a letter and forces the program
to run again if an error is found.
I have also added a continuation function to allow the programme to exit 
cleanly when the user is ready.
This version is set within a (while) loop using multiple 
definitions (def) that can be called repeatedly in this and other 
programs. 
This version gives the workings out for the user and exits cleanly.
'''

#
#
#========= ( DEFINITIONS OF FUNCTIONS )=========#
#
#

''' 
This function performs the main calculations for the program and 
prints the results on screen including the workings out for the sum.

To explain the first print statement, see sample code below:

name = 'maths'
number = 42
print '%s %d' % (name, number)

will print maths 42. 

Note that name is a string (%s) and 
number is an integer (%d for decimal)

'''

def triangle(base, height):		# Name of the function with arguments
	base = float(base)
	height = float(height)
	area = base * height / 2	# Perform calculation
	print "The working out is %d x %d / 2" % (base, height)
	print "Base x height =", base * height
	print "Once devided by 2 the area of your triangle is ",area
	
''' 
This Function performs a check of the user's input to make sure 
that it is a number and will not cause the programe to crash due to 
the user entering a string.
'''

def is_number(n):				#Name of the function with argument
	try:						#Attempt the following action
		float(n)				#Convert to float with argument
		return True				#If successful return True
	except ValueError:			#Check if error message is recieved
		return False			#If Error, return False
		
''' 
This function performs a check if the user would like to continue
and run another calculation, or to end the program. it returns a true
or a false value.
'''

def re_run(c):					#Name of Function with argument
	c.lower()					#Force string to Lower case
	if c == "y" or c == "yes":	#If one of these values are True then..
		return True				#End function with True value
	else:						#If both are False then..
		print "\nGood Bye\n"	#Print String
		return False			#End function with False value

#
#
#========= ( DEFINITIONS OF VARIABLES )=========#
#
#

''' 
This variable is what the while loop checks to see if it should 
loop again or not. Once set, a variable can be changed to any other 
value at any time 
'''

i = True						#Set variable to True

#
#
#========= ( DEFINITIONS OF PROGRAM LOOPS )=========#
#
#

# Start of loop, check if 'i' is true, otherwise do not loop
while i == True:
	print "\nThis programme calculates the area of a triangle\n"
	base = raw_input("Enter Base Value: ")
	height = raw_input("Enter Height value: ")
# Call function and check if both results return a True value
	if is_number(base) and is_number(height):
		
# Print contents of triangle function
		print triangle(base, height)

#If error or exception
	else:
		print "\nPlease enter numbers and not letters"
		
# Call continue function to change variable to true or false
# This will change the value of the variable 'i' above to either True 
# or False.

	i = re_run(raw_input("\nDo you wish to continue? Y/N "))



''' 
This version that will work with decimals, and wont break with letters
it will also loop over and over to allow for repeated use until
the user decides to quit.

This version has Error Checking and is very robust. 
These definitions can be taken and used in other programmes the user 
may create

Notice that the main programme is only 9 lines of code. if you want to 
change how it works, you do not have to change much. The previous 
verisons of the program would need a complete re-write.
'''
