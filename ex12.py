# Prompt the user with the string "How old are you? "
# assign the input to the variable age
age = raw_input("How old are you? ")
# Prompt the user with the string "How tall are you? "
# assign the input to the variable height
height = raw_input("How tall are you? ")
# Prompt the user with the string "How much do you weigh? "
# assign the input to the variable weight
weight = raw_input("How much do you weigh? ")

# Insert the age, height and weight variable into 
# the string format and display the string
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)