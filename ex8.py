# Create a string format and assign it to the variable formatter
formatter = "%r %r %r %r"

# Insert the integers 1, 2, 3 and 4 into 
# the string format and display the string
print formatter % (1, 2, 3, 4)
# Insert the strings "one", "two", "three" and "four" 
# into the string format and display the string
print formatter % ("one", "two", "three", "four")
# Insert the booleans True, False, False, True 
# into the string format and display the string
print formatter % (True, False, False, True)
# Insert the format into the sring and display it
print formatter % (formatter, formatter, formatter, formatter)
# Insert the strings into the format and display them
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)