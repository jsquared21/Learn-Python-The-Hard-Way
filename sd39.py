# create a mapping of provinces to abbreviation
provinces = {
	'Alberta': 'AB',
	'British Columbia': 'BC',
	'Manitoba': 'MB',
	'New Brunswick': 'NB',
	'Newfoundland and Labrador': 'NL',
	'Nova Scotia': 'NS',
	'Northwest Territories': 'NT',
	'Nunavut': 'NU',
	'Ontario': 'ON',
	'Prince Edward Island': 'PE',
	'Quebec': 'QC',
	'Saskatchewan': 'SK',
	'Yukon': 'YT'
}

# create a basic set of states and some cities in them
cities = {
	'AB': 'Edmonton',
	'BC': 'Victoria',
	'MB': 'Winnipeg',
	'NB': 'Frederiction',
	'NL': 'St. John\'s',
	'NS': 'Halifax',
	'NT': 'Yellowknife',
	'NU': 'Iqaluit',
	'ON': 'Toronto',
	'PE': 'Charlottetown'
}

# add some more cities
cities['QC'] = 'Quebec City'
cities['SK'] = 'Regina'
cities['YT'] = 'Whitehorse'

# print out some cities
print '-' * 10
print "ON Province has: ", cities['ON']
print "BC Province has: ", cities['BC']
print "QC Province has: ", cities['QC']

# print out some provinces
print '-' * 10
print "British Columbia's abbreviation is: ", provinces['British Columbia']
print "Nova Scotia's abbreviation is: ", provinces['Nova Scotia']
print "Prince Edward Island's abbreviation is: ", provinces['Prince Edward Island']

# do it by using the province then cities dict
print '-' * 10
print "Ontario has: ", cities[provinces["Ontario"]]
print "Quebec has: ", cities[provinces["Quebec"]]
print "Alberta has: ", cities[provinces["Alberta"]]

# print every province abbreviation
print '-' * 10
for province, abbrev in provinces.items():
	print "%s is abbreviated %s" % (province, abbrev)

# print every city in province
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for province, abbrev in provinces.items():
	print "%s province is abbreviated %s and has city %s" % (
		province, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by province that might not be there
province = provinces.get('Texas')

if not province:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city