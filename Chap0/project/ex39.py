#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
states = {
    'oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities:
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY states has: ", cities['NY'])
print("OR states has: ", cities['OR'])

# print out some cities
print('-' * 10)
print("Michigan's abb is: ", states['Michigan'])
print("Florida's abb is: ", states['Florida'])

# print some states
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# do it by using the state abbreviation
print('-' * 10)
for state, abbrev in list(sates.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    print(f"and has city {cities[abbrev]}")

# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"the city for the state 'TX' is: {city}")
