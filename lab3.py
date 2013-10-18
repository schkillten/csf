series = raw_input("Select if you would like to get the Fibonacci number or a Sum: ")
n = input("Enter the number in which you would like calculated: ")


series = series.lower()
series = series[0]





if series == "f":
	pp = 0
	p = 1
	for i in range(n - 1):
		total = pp + p
		pp = p
		p = total
	print total
elif series == "s":
	total = 0
	for i in range(n + 1):
	
		total = total + (3*i)
	print total
else:

	print "Invalid string."
