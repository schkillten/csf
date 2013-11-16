# Name: Kyle schaefer
# Group: 22
# Doing group 7's questions

# Prob 3: What is assert doing:

a = 5
b = 5

print "A", a
print "B", b
assert a == b

# The assert it checking if the values of a and b are equal

b = 10

print "New B", b

# assert a == b (Commented out so I can complete the rest of the program.)

# At this point it gives an error since a is no longer equal to b

### Prob 4

c = 2

def dv(x,y,z): return float(x+y) / z


print "The result of the dv function: ", dv(a,b,c)


### Prob 5

names = ("Henry", "BOB", "JIMMY", "PAUL")

ages = [23, 34, 213, 432]

phone_num = {"Mother" : 12345678910}
print

print names,ages,phone_num

### Prob 6

list_a = [1,2,3,4,5]
list_b = [5,4,3,2,1]
print "\nThis is list_a: ", list_a
print "This is list_b: ", list_b


list_c = []

for i in range(len(list_a)):
	list_c.append(list_a[i] + list_b[i])

print "This is list_c: ", list_c


### Prob 7

prob_list = ["\napple", "orange", "pear"]

for i in prob_list:
	print i


