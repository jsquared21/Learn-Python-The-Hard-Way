# Import the function argv from the sys module
from sys import argv

# Assight the argument variables to 
# the variables script and input_file
script, input_file = argv

# Create a function named print_all that takes one argument
# call the read function on the argument and display its contents
def print_all(f):
	print f.read()

# Create a function named rewind that takes one argument call the 
# seek function on the argument to return to the start of the file
def rewind(f):
	f.seek(0)

# Create a function named print_a_line that takes two arguments.
# Display the first argument. Calls the readline function on
# the second argument and displays it contents
def print_a_line(line_count, f):
	print line_count, f.readline()

# Call the open function with the variable input_file and 
# assign the result to the variable current_file
current_file = open(input_file)

# Diaplay a string and start a new line
print "First let's print the whole file:\n"

# Call the print_all function with the variable current_file
print_all(current_file)

# Display a string
print "Now let's rewind, kind of like a tape."

# Call the rewind function with the variable current_file
rewind(current_file)

# Display a string
print "Let's print three lines:"

# Assign the number 1 to the variable current line
current_line = 1
# Call the print_a_line function with the variables
# current_line and current_file
print_a_line(current_line, current_file)

# Add 1 to the variable current_line
current_line = current_line + 1
# Call the print_a_line function with the 
# variables current_line and current_file
print_a_line(current_line, current_file)

# Add 1 to the variable current_line
current_line = current_line + 1
# Call the print_a_line function with the 
# variables current_line and current_file
print_a_line(current_line, current_file)