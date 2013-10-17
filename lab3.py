series = raw_input("Enter in a word: ")
n = input("Enter in a number: ")

print series


if series == "fibonacci":
	pp = 0
	p = 1
	for i in range(n - 1):
		total = pp + p
		pp = p
		p = total
	print total

if series == "sum":
	total= 0
	for i in range(n + 1):
		total = total + (3*i)

	print total
