# Import the argv method from the sys module
from sys import argv

# Assign the arguments in the arguement variable to 
# the variables script and user_name respectively
script, user_name = argv
# Assign the character '>' to the prompt variable
prompt = '> '

# Insert the variables user_name and script 
# into the string format and display the string
print "Hi %s, I'm the %s script." % (user_name, script)
# Display a string
print "I'd like to ask you a few questions."
# Insert the variable user_name into the 
# formatted string and display the string
print "Do you like me %s?" % user_name
# Prompt the user for input and assign the input to the variable likes
likes = raw_input(prompt)

# Insert the variable user_name into the
# formatted string and display the string
print "Where do you live %s?" % user_name
# Prompt the user for input and assign the input to the variable lives
lives = raw_input(prompt)

# Display the string
print "What kind of computer do you have?"
# Prompt the user for input and assign the input to the variable computer
computer = raw_input(prompt)

# Insert the variables likes, lives and computer 
# into the mutiline format string and display the string
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)