# Display the string "How old are you?" remove the new line symbol
print "How old are you?",
# Prompt the using to input data and assign it to the variable age
age = raw_input()
# Display the string "How tall are you?" and remove the new line symbol
print "How tall are you?",
# Prompt the user to input data and assign it to the variable height
height = raw_input()
# Display the string "How much do you weigh?" and remove the new line symbol
print "How much do you weigh?",
# Prompt the user to enter data and assign it to the variable weight
weight = raw_input()

# Insert the variables age, height and weight 
# into the formatted string and display it
print "So, your're %r old, %r tall and %r heavy." % (
	age, height, weight)