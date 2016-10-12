m = int(raw_input("Variable must be an integer Which multiplication table would you like?:"))
x = int(raw_input("This must also be an integer How high do you want to go?:"))
if x <= 0:
    x = int(raw_input("Sorry this number must be greater than 0(How high do you want to go?):"))
print "Here is your multiplication table of", m,"up to", x
for i in range(1,x+1):
    print m, "times", i,"=", i*m