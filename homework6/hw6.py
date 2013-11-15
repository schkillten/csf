# Name: Kyle Schaefer, Ahmed Ali
# Username: schkyl10 , aliahm18
# Homework 6 (tutorial program)


"""
    
	Five Key Concepts for being able to complete problem 1 from homework 5
	1. Understanding dictionaries and being able to use the keys and the benefits of using them
	2. Understanding For loops.
	3. Understanding calling and defining functions.	
	4. Understanding the scopes like when to indent and unindent
	5. Understanding Indexing and the difference with indexing on dictionaries and lists
	note: not in this order
"""
"""


dictionary = {}
dictionary["Kyle"] = 10
dictionary["Ahmed"] = 5
# Problem 1 (Dictionaries and lists)
# Difference between lists and dictionaries
# A dictionary is noted with {} similar to a set, however an example of a dictionary would have a ":" inside of the brackets
# the reason for this is because a dictionary has keys and values, such as,
print "This is an example of a dictionary."

print dictionary
part1 = raw_input("You go ahead and create your own dictionary: ")
print part1
print "This is the name of the dictionary and the contents within it:", 'dictionary = {"Kyle" : 10, "Ahmed" : 5}'

# This dictionary shows everyones favorite number.
# The term Kyle is the first key listed in this dictionary (dictionaries order does not matter) and would yield the value of 10 if the key "Kyle" was called.
# If the key "Ahmed" was called it would yield the value of 5
print "Example of how to call a key in a dictionary: dictionary[\"Kyle\"]"
print "Would return: ", dictionary["Kyle"]
print "Another example: dicionary[\"Ahmed\"]"
print "Would return: ", dictionary["Ahmed"]
# The next concept to understand with dictionaries is how to add another key and value to the dictionary.
print "An example of adding contents to a dictionary would look like this: dictionary[\"Ian\"] = 14"
dictionary["Ian"] = 14
print "To see the new content in the dictionary, you would simply type the name of the dictionary: dictionary"
print "Would return: ", dictionary
"""

print "First concept we will introduce is dictionaries." 
print "Here is an example of the contents in a dictionary: "
dictionary = {"Kyle" : 10, "Ahmed" : 5}
print dictionary

print "\nThe way you name a dictionary is the same as a variable,"
print "as long as its not reserved by python its fine to use it."
print "Go ahead and create a dictionary, lets make an empty dictionary for now,"
print "should look like this: <dictionary name> = {}."
print "Name the dictionary \"test_diction\""
user_diction = raw_input("\nEnter here: ")

test_diction = {}

leave = "n"
while leave == "n":
	if user_diction == "test_diction = {}":
		print "Correct!"
		leave = "y"
	else:
		print "Incorrect"
		print "Remember it should be and empty ditctionary like this: <dictionary name> = {}."
		user_diction = raw_input("Try again: ")
move_on = raw_input("Press enter to move on: ")

print "\nGood so now we want to add contents to the dictionary."
print "Adding contents is simple, you name the key and give it the value."
print "An example would look like this: "
print "test_diction[\"Ian\"] = 14"
print 'The key being "Ian" and the value being "14"'


move_on = raw_input("Press enter to move on: ")
print "\nSo now we are going to have you go ahead and add some content to your dictionary."
print "The dictionary we will make will be of fruits and their prices, name your first key apple,"
print "and the value of it is 0.45 cents. (dont put the word cents just the number)"
print "Using the dictionary you already made named \"test_diction\""
user_add = raw_input("Enter here: ")

test_diction["apple"] = "0.45"

leave = "n"
while leave == "n":
	if user_add == 'test_diction["apple"] = 0.45' or user_add == 'test_diction["Apple"] = 0.45':
		print "Correct!"
		leave = "y"
	
	else:
		print "Incorrect"
		print 'Remember we want a key name "apple" and a value of "0.45"'
		user_add = raw_input("Try again: ")

move_on = raw_input("Press enter move on: ")

print "\nGreat now you can make a dictionary and add content into it!"
print "Your current dictionary should look like this: "
print '{"apple" : 0.45}'

move_on = raw_input("Press enter to move on: ")

print "\nNow we want you to go ahead and add a few more items,"
print "go ahead and make two new keys, first named pear with the value of 1.00,"
print "and cherries valued at 2.50. Do the pear first then the cherries"
pear_key = raw_input("Enter here: ")

leave = "n"
while leave == "n":
	if pear_key == 'test_diction["pear"] = 1.00' or pear_key == 'test_diction["Pear"] = 1.00':
		print "Great!"
		leave = "y"

	else:
		print "Incorrect."
		print "If you cannot remember how to add content into you dictionary scroll back up."
		pear_key = raw_input("Try again: ")

print "\nNow do the cherries key and value."
cherries_key = raw_input("Enter here: ")
leave = "n"
while leave == "n":
	if cherries_key == 'test_diction["cherries"] = 2.50' or cherries_key == 'test_diction["cherries"] = 2.50':
		print "Great!"
		leave = "y"
	else:
		print "Incorrect!"
		print "Scroll back up if you cannot remember how to add conent into the dictionary."
		cherries_key = raw_input("Try again: ")
move_on = raw_input("Press enter to move on.")

test_diction["pear"] = 1.00
test_diction["cherries"] = 2.50

print "\nAlright now you have a dictionary with a few keys and values in it."
print "This is what your dictionary should look like so far: "
print test_diction
move_on = raw_input("Press enter to move on: ")



print "\nNow that you are able to add content into the dictionary we'll show you how to index it."
print "Lists and dictionaries are a little different with indexing."
print "With a given list named lista = [25,42,13,46]."
print "lista[2] would return 13. With dictionaries you have to call the key."

move_on = raw_input("Press enter to move on: ")

print '\nAn example from my first dictionary would look like this: dictionary["Ahmed"]'
print "Would return: ", dictionary["Ahmed"]
print "Go ahead and access the pear key so we can get its value."
key_user = raw_input("Enter here: ")
leave = "n"
while leave == "n":
	if key_user == 'test_diction["pear"]':
		print "Correct!"
		print test_diction["pear"]
		leave = "y"
	
	else:
		print "Incorrect!"
		print "If you need help scroll up on how to index a dictionary."
		key_user = raw_input("Try again: ")

move_on = raw_input("Press enter to move on:")


print "\nNow we will introduce nested data structures."
print "An example of a nested data structure is similar to nested loops."
print "There is a number of different types of data structures, we will use lists and dictionaries."
print "Here is an actual example of what one might look like: "
print
dictionary["Ian"] = 14
lista = [dictionary, test_diction]
print lista	

print '\nSo this example is a list, with two dictionaries inside of it. We will call this "lista"'

move_on = raw_input("\nPress enter to move on:")

print "Now we want to index a specific key inside of the nested data structure."
print "The syntax of what it would look like grabbing a key from a dictionary that is inside a list."
print '<name of list>[index][key]'
print '\nA random example: listname[0]["honda"]'
print "This would return the 0th dictionary and the key value of honda within the dictionary."
print "So from our example earlier of a nested data structure,the one called lista,"
print "how would you get the value 14 to be printed from it?"
user_attempt = raw_input("Enter here: ")
leave = "n"
while leave == "n":
	if user_attempt == 'lista[0]["Ian"]':
		print lista[0]["Ian"]
		print "Correct!"
		leave = "y"
	else:
		print "Incorrect!"
		print "Remember we want the value of a key, so we need to index the dictionary"
		print "that the value 14 is in, and use that key to print 14."
		user_attempt = raw_input("Try again: ")


move_on = raw_input("\nPress enter to move on: ")

print "So now you can make dictionaries, and you know how to index nested data structures, "
print "but now you need to know how to make the nested data structures."
print "We will continue to use the same form, a list with dictionaries inside of it."
print "\nNote that this is not the only type of a nested data structure, "
print "you could have dictionaries with lists inside of them, or even keys, with lists as its value."
print "Or many others that we wont go over here."
move_on = raw_input("\npress enter to move on: ")

print "\nThere are several ways to make a nested data structure, we will stick to a simple one."
print "And a way we think is a clean way to do it, specifically with lists with dictionaries inside."
print "First you can make the dictionaries, such as: "

dict1 = {"Apple" : 1.00, "Bananas": 1.25, "Pear" : 1.00}
dict2 = {"Apple" : 1.25, "Bananas" : 1.45, "Pear" : 1.50}

print "\n","dic1 =",  dict1
print "dic2 =", dict2

move_on = raw_input("Press enter to move on: ")

print "\nThen you need to make the list with the dictionaries inside of it, we will call it nest_list: "
nest_list = [dict1, dict2]

print "\nnest_list = [dict1,dict2]"
print "\nThe result would look like this: "
print nest_list

print '\nSo using our two dictionaries names "dictionary" and "test_diction",'
print "make a nested data structure. You can call it nested_list."
print "\nNote that since its a list, with dictionaries inside, the order does matter, "
print 'so lets order it with "dictionary" first and "test_diction" next.'

nested_list = [dictionary, test_diction]

user_nest = raw_input("\nEnter here: ")
leave = "n"

while leave == "n":
	
	if user_nest == 'nested_list = [dictionary, test_diction]':
		print nested_list
		print "Correct!"
		leave = "y"

	else:
		print "Incorrect!"
		print "Look at the examples if you're having a hard time remember how to make the structure."
		user_nest = raw_input("Try again: ")

move_on = raw_input("Press enter to move on: ")





print "Alright so now you can make a nested data structure for our purpose."
print "Next we want to understand for loops and how useful they can be with lists and dictionaries."

print "\nFirst we will look at a simple for loop: "
print "\nfor i in range(10):"
print "    print i"
print "Should return this: "
for i in range(10):
	print i

move_on = raw_input("\nPress enter to move on: ")

print "For loops don't just use the range function, they can be used for most any sequence."
print "The syntax of a for loop would look like this:"
print "for <variable name> in <seqence>:"
print "    <do code until loop is over> "

move_on = raw_input("\nPress enter to move on: ")

print "An example of another tpye would be:"
print 'for i in "Sequence": '
print "    print i "
print "\nShould return: "
for i in "Sequence":
	print i

move_on = raw_input("\nPress enter to move on:")


print "\nNow we can show you how useful a for loop can be with data structures, such as a list:"
print "test_list = [5,3,2,7,3,1,4,6,7]"
print "for i in test_list:"
print "    print i"
print "Would return this: "
test_list = [5,3,2,7,3,1,4,6,7]
for i in test_list:
	print i


move_on = raw_input("\nPress enter to move on:")

print "\nNow we want to go through a dictionary with a for loop: "
print "We can even use the exisiting dictionary we already made named test_diction."
print "for i in test_diction:"
print "    print i"
print "\nWould return this: "

test_diction = {"apple" : 0.45, "cherries" : 2.50, "pear" : 1.00}
for i in test_diction:
	print i


dict1 = {"Apple" : 1.00, "Bananas": 1.25, "Pear" : 1.00}
dict2 = {"Apple" : 1.25, "Bananas" : 1.45, "Pear" : 1.50}

nest_list = [dict1, dict2]

move_on = raw_input("Press enter to move on:")


print "Now we can go through a nested data structure using the nested structure we made earlier named nest_list, like so: "
print "for i in nest_list:"
print "    print i"

print "\nShould return: "
for i in nest_list:
	print i

move_on = raw_input("Press enter to move on: ")



print "\nSo now we want to be able to go through specific items in the nested data structure, "
print "to do this we would type something like this: "
print "for i in range(len(nest_list)):"
print '    print nest_list[i]["Apple"]'



for i in range(len(nest_list)):
	print nest_list[i]["Apple"]

print "\nSo this loop is using the len() function, which grabs the length of the nest_list, having 2 dictionaries inside of it, "
print "gives it the length of 2. The indent on the inside of the for loop prints the nest_list[i], the first iteration is 0 "
print 'so it would print the 0th dictionary, then the nest part is asking for the key "Apple", which returns the value of apple.'
print 'The next iteration through the loop turns the "i" into a 1, and prints the "Apple" value in the second dictionary.'


move_on = raw_input("Press enter to move on: ")

print "\nNow we will have you go ahead and print out the values of the \"Pear\" in each dictionary using a for loop."
print "Using the same list, nest_list."
user_loop = raw_input("Enter here: ")


print "\nFirst we will have you do the for loop setup, then after that we will write the second half of the code."

leave = "n"
while leave == "n":

	if user_loop == "for i in range(len(nest_list)):":
		print "Correct!"
		leave = "y"

	else:
		print "Incorrect!"
		print "Use the example above to help you with the setup of the for loop, should be the same."
		user_loop = raw_input("Try again: ")


loop_scope = raw_input("Enter here: ")

leae = "n"
while leave == "n":

	if loop_scope == 'print nest_list[i]["Pear"]':
		print "Correct!"
		leave = "y"


	else:
		print "Incorrect!"
		print "Look at the example above to help with the format."
		loop_scope = raw_input("Try again: ")

print "\nAwesome! Now we will run the same loop but we will use a function inside of the loop to tell us which store has the lowest prices."



from math import sqrt

print "So to start off we will recall how to call functions. An example of a function call would be: sqrt():"
print "The name of this function is sqrt, the parameters would go into the brackets and would return the square root of the arguement entered."
print "An example would be: "
print "sqrt(25)"
print "Would return: "
print sqrt(25)


move_on = raw_input("Press enter to move on: ")

print "\nYou can also use functions inside of a loop, say we want to get the sqaure root of all the numbers from 25 to 50:"
print "for i in range(25,51):"
print "    print sqrt(i)"
print "Would return: "

move_on = raw_input("Press enter to move on: ")
print
for i in range(25,51):
	print sqrt(i)

move_on = raw_input("Press enter to move on: ")

print "\nWe could even get the square root of each number between 25-50 and put it into a list to store it:"

print "First we need to set an empty list up outside of the loop to have content added into it inside of the loop:" 
print "alist = []"
print "\nfor i in range(25,51):"
print "    alist.append(sqrt(i))"
print "\nWould return this:"

alist = []

for i in range(25,51):
	alist.append(sqrt(i))

print alist

move_on = raw_input("Press enter to move on: ")

def square(x): return x*x

print "So now we will have you go ahead and use a for loop similar to ours, but instead we will use a different function."
print "This function is called square(). It takes one arguement just like the sqrt function, we want you to make an empty list, "
print 'name the empty list "empty_list". We want you to add the first ten numbers (1-10) and get the square of each number then add '
print "it to the list you made."

move_on = raw_input("Press enter to move on: ")

print 'Remeber to start with making an empty list name "empty_list".'

emptylist = raw_input("Start here: ")

leave = "n"
while leave == "n":
	if emptylist == "empty_list = []":
		print "Correct!" 
		leave = "y"

	else:
		print "Incorrect!"
		print "Use the example from above to help setting up."
		emptylilst = raw_input("Try again: ")

print "Great! Now lets make the for loop, remember the range is 1-10:"

move_on = raw_input("Press enter to move on: ")

for_loop = raw_input("Enter here: ")


leave = "n"
while leave == "n":

	if for_loop == "for i in range(1,11):":
		print "Correct!"
		leave = "y"

	else:
		print "Incorrect!"
		print "Look at the example above, only difference is the numbers between the range."
		for_loop = raw_input("Try again: ")

print "Great now the last part is putiing the information into the list."

move_on = raw_input("Press enter to move on:")

add_to_list = raw_input("Enter here: ")

leave = "n"

while leave == "n":

	if add_to_list == "empty_list.append(sqrt(i))":

		print "Correct!"

		leave = "y"

	else:

		print "Incorrect!"
		print 'The code should look similar to the for loop we showed you earlier just a different name instad of "alist"'
		add_to_list = raw_input("Try again: ")



print "Waaaahooooooo look behind you!"


print "\nJust kidding you're done...."
