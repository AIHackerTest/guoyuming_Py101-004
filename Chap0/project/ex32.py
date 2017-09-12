#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


# you need a way to store the results of loops somewhere. SO I did it right in ch1's assignment, where I create a list to store searching loop. 

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"this is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it for i in change
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a functon that lists understand
    elements.append(i)
    print(elements)

# now we can pirnt them out too
for i in elements:
    print(f"Element was: {i}")