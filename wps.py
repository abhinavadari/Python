p = float(raw_input("Enter your purchase price:"))
if p <= 10:
	print "You got a 10% discount"
	fp = float(p - .1p)
if p > 10:
	print "You get a 20% discount"
	fp = float(p - .2p)
print "Your total is %f"% fp