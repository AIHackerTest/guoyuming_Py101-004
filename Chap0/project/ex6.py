#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define a variable with integer 10
types_of_people = 10
# define a varibale named x, though a bad name with formatted string embedded with a variable
x = f"There are {types_of_people} types of people."

# define two variable with string
binary = "binary"
do_not = "don't"

# define a variable y with values similar to x
y = f"Those who know {binary} and those who {do_not}."

# exert the function of printing variable x and y, and with strings
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")


# define a Boolean variable as 
hilarious = False
# define a variable with string embeded with another variable that is not defined 
joke_evaluation = "Isn't that joke so funny?! {}"

# exert print function 
print(joke_evaluation.format(hilarious))

# define two variable with strings 
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)