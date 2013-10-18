series = raw_input("Would you like the fibonacci number or sum of 3's (Fibonnaci/Sum): ")
n = input("Enter the number in which you would like calculated: ")

# takes the string and makes everything lowercase
series = series.lower()
# takes the lowercase string and grabs just the first element of the string
series = series[0]




# this statement/loop determines if its for the fibonacci number, then calculates according to n
if series == "f":
	pp = 0
	p = 1
	for i in range(n - 1):
		total = pp + p
		pp = p
		p = total
	print total
	
# this statement is for the sum of multiples of 3 up to n
elif series == "s":
	total = 0
	for i in range(n + 1):
	
		total = total + (3*i)
	print total
else:

	print "Invalid string."
