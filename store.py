p = float(raw_input("What’s your purchase price?"))
if p <= 10:
	print "You got a 10% discount"
	fp = float(p - .1%p)% p
if p > 10:
	print "You get a 20% discount"
	fp = float(p - .2%p)% p
print "Your total is %f"% fp