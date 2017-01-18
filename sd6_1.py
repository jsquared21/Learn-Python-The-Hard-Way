# Assign a formatted string to the variable x
x = "There are %d types of people." % 10
# Assign the string "binary" to the variable binary
binary = "binary"
# Assign the string "don't" to the variable do_not
do_not = "don't"
# Insert the string binary and the string do_not into the 
# formatted string and assign the result to the variable y

# Display the contents of the variable x
print x
# Display the contents of the variable y
print y

# Insert the variable x in to a formatted string and display its contents
print "I said: %r." % x
# Insert the variable y in to a formatted string and display its contents
print "I also said: '%s'." % y

# Assign the boolean False to the variable hilarious
hilarious = False
# Assign the formatted string to the variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Insert the boolean hilarious into the variable 
# joke_evaluation and display its contents
print joke_evaluation % hilarious

# Assign a string to the variable w 
w = "This is the left side of..."
# Assign a string to the variable e 
e = "a string with a right side"

# Concatenate the string in the variable e into the 
# string in the variable w and display its contents
print w + e