#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define a variable with string but embedded with {} character to hold variables
formatter = "{} {} {} {}"

# print the variable formatter with values that contain integers, by introducing .format syntax
print(formatter.format(1, 2, 3, 4))

# like the previous one, but values are strings
print(formatter.format("one", "two", "three", "four"))

# this time, the value types are Boolean values
print(formatter.format(True, False, False, True))

# will this line print out a lot of {}s ? variable in themselves, {} not contain value?
print(formatter.format(formatter, formatter, formatter, formatter))

# easy, containt strings edited in each line 
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# predicting the last two print fucntion, I got one right and one wrong. The right one is the last but one, which exports lots of {} without meaning values. The didn't export strings in different but in one line with space, and if you delete a comma, error reported. So they are just different strings used comma to seperate. 