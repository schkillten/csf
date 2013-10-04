# Name: Kyle Schaefer
# Evergreen Login: schkyl10
# Computer Science Foundations
# Programming as a way of life
# Homework 1


import math
import sys

#problem 1 of the homework solving the quadractic
#this is for the subtraction half of the quadratic general solution
def quad_minus(a,b,c):
	root =(-b - math.sqrt((b**2) + (-4*a*c))) / (2*a)
	return str(root)

#this is for the addition half of the quadratic general solution
def quad_plus(a,b,c):
	root =(-b + math.sqrt((b**2) + (-4*a*c))) / (2*a)
	return str(root)
	
#takes user input so any quadratic equation can be solved if all three values are valid
a = input("Enter the value of A: ")
b = input("Enter the value of B: ")
c = input("Enter the value of C: ")


if (4*a*c) > (b**2):
	print "This is an imaginary number. Not currently setup for imaginary numbers"
	sys.exit(0)

#solves for the first half of equation
root = quad_minus(a,b,c)
print "This is root #1: %s." % (root)
print "The  \"tpye\" of root #1 is: ", type(root)
#solves for the second half of equation
root = quad_plus(a,b,c)
print "This is root #2: %s." % (root)
print "The  \"tpye\" of root #2 is: ", type(root)
#problem 2 of homework importing the mod with values a-f
from hw1_test import *

 #problem 3 of homework solving the equation using values from hw1
answer = ((a and b) or (not c) and not (d or e or f))

print "The answer for part 3: ", answer

#this took about an hour to get working at this point. I am familiar to python syntax which was useful
#but the readings and lectures i feel did have the information required to complete this program
