numbers = [] 
increments = 0

def sd1(r):
	i = 0
	while i < r:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	
def sd3(r, increments):
	i = 0
	while i < r:
		print "At the top i is %d" % 1
		numbers.append(i)

		i += increments
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 


def sd5(r):
	for i in range(0, r):
		print "At the top i is %d" % i
		numbers.append(i) 

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

print "\nCall function for study drill 1 with 6 as its argument"
sd1(6);
print "The numbers: "

for num in numbers:
	print num

numbers = [] # Empty the list
print "\nCall function for study drill 3 with 6 and 2 as arguments"
sd3(6, 2)
print "The numbers: "

for num in numbers:
	print num

numbers = [] # Empty the list
print "\nCall function for study drill 5 with 6 as its argument"
sd5(6)
print "The numbers: "

for num in numbers:
	print num