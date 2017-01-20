# Import the argv method from the sys module
from sys import argv

# Assign the arguments in the argument variable 
# to the variables script and filename
script, filename = argv

# Call the method open with filename as its argument
# and assign the result to the variable txt
txt = open(filename)

# Insert the variable filename into the 
# string format and display the string
print "Here's your file %r:" % filename
# Call the method read with no arguments on 
# the txt variable and display its contents
print txt.read()

# Call the method close with no arguments on the variable txt
txt.close()

# Display a string
print "Type the filename again:"
# Prompt the user to insert the filename 
# and assign the input to file_again
file_again = raw_input("> ")

# Call the method open with file_again as its argument
# assign the result to the variable txt_again
txt_again = open(file_again)

# Call the method read with no arguments on the 
# variable txt_again and display its contents
print txt_again.read()

# Call the method close with no arguments on the variable txt_again
txt_again.close()