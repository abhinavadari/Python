nb = int(raw_input("How many blocks of stars do you want?"))
nl = int(raw_input("How many lines of stars do you want?"))
ns = int(raw_input("How many stars do you want?"))
for block in range (0, nb):
	for line in range (0, nl):
		for star in range (0, ns):
			print "*",
		print 
	print 