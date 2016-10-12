n1 = float(raw_input("Enter the first number: "))
n2 = float(raw_input("Enter the second number: "))
if n1 < n2:
	print n1,"is less than",n2
if n1 > n2:
	print n1,"is greater than",n2
if n1 == n2:
	print n1,"is equal to",n2
if n1 != n2:
	print n1,"is not equal to",n2	
if n1 >= 10:
	print "You got at least ten!"
elif n1 >= 5:
	print "You got at least 5!"
else:
	print "You got less than 5."