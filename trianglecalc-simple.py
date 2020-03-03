#! /usr/bin/env python
""" Programme created by Leigh Wilson 3/2015
A Simple calculator that works out the area of
a triangle using the base x height devided by 2 method """

print "This programme calculates the area of a triangle from 2 values"
base = raw_input("Enter base value: ")
base2 = int(base)
height = raw_input("Enter height value: ")
height2 = int(height)
area = base2 * height2 / 2
print "The area of your triangle is ",area


#Simple version that will not work with decimal numbers.

#Change "int()" to float() and decimal numbers will calculate correctly
