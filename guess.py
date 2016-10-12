import random
s = random.randint(1,99) # Picks secret integer
guess = 0
tries = 0
print "Pick a 'secret' number from 1 to 99 only 6 tries"
while guess != s and tries < 6:
	guess = int(raw_input("What is your guess?:")) # Gets player's guess
	if guess < s:
		print "Too low!"
	elif guess > s:
		print "Too high!"
	tries = tries + 1 # Uses up one try
if guess == s:
	print "You found the number!!"
else:
	print "Try again you lost,:)"
	print "My 'secret' number was %d" %s