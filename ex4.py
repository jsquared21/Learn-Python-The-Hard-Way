cars = 100 # Assign 100 to the variable cars
space_in_a_car = 4.0 # Assign 4.0 to the variable space_in_a_car
drivers = 30 # Assign 30 to the variable drivers
passengers = 90 # Assign 90 to the variable passengers
# Subtract drivers from cars and Assgin the 
# result to the variable cars_not_driven
cars_not_driven = cars - drivers 
cars_driven = drivers # Assign drivers to the variable cars_driven
# Multiply cars_driven by space_in_a_car 
# and Assign the result to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Divide passengers by cars_driven and assign 
# the result to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# Display the number of cars available
print "There are", cars, "cars available."
# Display the number of drivers available
print "There are only", drivers, "drivers available."
# Display the number of cars not driven today
print "There will be", cars_not_driven, "empty cars today."
# Display todays carpool capacity
print "We can transport", carpool_capacity, "people today."
# Display the number of passengers today
print "We have", passengers, "to carpool today."
# Display the average passengers per car 
print "We need to put about", average_passengers_per_car, "in each car."