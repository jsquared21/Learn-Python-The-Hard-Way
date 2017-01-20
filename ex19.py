# Create a cheese_and crackers function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Insert the first argument into a formatted string and display it
	print "You have %d cheese!" % cheese_count
	# Insert the second argument into a formatted string and display it
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# Display a string
	print "Man that's enough for a party!"
	# Display a string with a new line character at the end
	print "Get a blanket.\n"


# Display a string
print "We can just give the function numbers directly:"
# Call the cheese_and_crackers function with numbers
cheese_and_crackers(20, 30)

# Display a string
print "Or, we can use variables from our script:"
# Assign the number 10 to the variable amount_of_cheese
amount_of_cheese = 10
# Assign the number 50 to the variable amount_of_crackers
amount_of_crackers = 50

# Call the cheese_and_crackers function using variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Display a string
print "We can even do math inside too:"
# Call the cheese_and_crackers function with math
cheese_and_crackers(10 + 20, 5 + 6)


# Display a string
print "And we can combine the two, variables and math:"
# Call the cheese_and_crackers function with math, numbers and variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)