name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
inches_to_cm = 2.54 # centimeters in an inch
height_in_cm = height_in_inches * inches_to_cm # height in centimeters
weight_in_lbs = 180 # lbs
lbs_to_kgs = 0.453592 # kilograms in a pound
weight_in_kgs = weight_in_lbs * lbs_to_kgs # weight in kilograms 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height_in_cm
print "He's %d kilograms heavy." % weight_in_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	age, height_in_inches, weight_in_lbs, age 
	+ height_in_inches + weight_in_lbs)