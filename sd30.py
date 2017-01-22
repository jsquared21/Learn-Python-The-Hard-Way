# Assign 30 to the variable people
people = 30
# Assign 40 to the variable cars
cars = 40
# Assign 15 to the variable trucks
trucks = 15


# If cars is greater than people display "We should take the cars."
if cars > people:
	print "We should take the cars."
# Else if cars is less than people display "We should not take the cars."
elif cars < people:
	print "We should not take the cars."
# Else display "We can't decide"
else:
	print "We can't decide."

# If trucks is greater than cars display "That's too many trucks."
if trucks > cars:
	print "That's too many trucks."
# Else if trucks is less than cars display "Maybe we could take the trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
# Else display "We still can't decide."
else:
	print "We still can't decide."

# If people is greater than trucks display "Alright, let's just take the trucks."
if people > trucks:
	print "Alright, let's just take the trucks."
# Else display "Fine, let's stay home then."
else:
	print "Fine, let's stay home then."