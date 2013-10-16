# Name: Kyle Schaefer
# Evergreen Login: schkyl10
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

#problem 1 for gauss's problem

## This is the function used to solve problem 1

# This function adds consecutive numbers up to the amount entered using a while loop
def gauss(gauss_prob):

	# These first two variables are used to start the sequence
	total = 1
	p = 2
	
	while gauss_prob > 1:
		gauss_prob = gauss_prob - 1
		total = total + p
		p = p + 1
		
	return total

## This is the function used to solve problem 2


#this function takes a number say 10 and prints each 
def recip(recip_range):

	for i in range(1,recip_range):
		recip_range = 1.0 / i
		print recip_range

## This is the function used to solve problem 3

## This function calculates the triangular numbers
def triang(triang_num):

	# Identity for addition
	total = 0
	for i in range(1, triang_num + 1):
		total = total + i

	return total
	
## This is the function used to solve problem 4

## This function calculates factorials
def fact(factorial):

	# Identity for multiplication
	total = 1
	
	for i in range(1, factorial + 1):
		total = total * i
	
	return total
	
## This is the function used to solve problem 5

## This function prints each factorial down from whatever the input is
def revfact(fact_range):
	fact_range = fact_range + 1
	for i in range(1, fact_range + 1):
		fact_range = fact_range - 1
		total = 1
		for i in range(1, fact_range + 1):
			total = total * i
		print total
		
## This is the function used to solve problem 6

## This function gets the reciprocal of any factorial and adds the total
def sumrecipfact(total_range):
	total = 1
	sumtot = 1
	for i in range(1,total_range + 1):
		total = total * i
		recip = 1.0 / total
		sumtot = sumtot + recip
	return sumtot


## This is the statisfy the import part of the first problem and to solve for n, however the next part of the program labeled problem 1 takes user input to solve for any n for the same problem.
from hw2_test import n

hw2_test = gauss(n)
print "\nThis is the answer received by importing n from mod hw2_test:", hw2_test


	
##
## Problem 1
##

print "\nProblem 1 solution follows:"

natural_num = input("\nWhat range of natural numbers do you wanted added: ")
natural_num = gauss(natural_num)
print "\nThe total sum of these natural numbers: ", natural_num

##
## Problem 2
##

print "\nProblem 2 solution follows:"

recip_num = input("\nEnter the range of numbers in which you want the reciprocal of: ")
print "\nThese are the reciprocals:"
recip_num = recip(recip_num)

##
## Problem 3
##

print "\nProblem 3 solution follows:"

triang_num = input("\nSWhat triangular number would you like: ")
triang_num = triang(triang_num)
print "\nThe triangular number is:", triang_num

##
## Problem 4
##

print "\nProblem 4 solution follows:"

num_factori = input("\nWhat factorial would you like calculated: ")
num_factori = fact (num_factori)
print "\nThe factorial Is:", num_factori


##
## Problem 5
##

print "\nProblem 5 solution follows:"

test = input("\nThis is to get the factorials of every number up to what you enter: ")
test = revfact(test)

##
## Problem :
##

print "\nProblem 6 solution follows:"

recipfact = input("\nEnter the number you want the sum of reciprocals of factorials: ")
recipfact = sumrecipfact(recipfact)
print "\nThe sum of all the reciprocals of all the factorials you wanted is:", recipfact

print "\n\nThanks for looking at my homework!"
