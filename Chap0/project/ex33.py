#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# a while-loop will keep executing the code block under it as long as a boolean expression is True. Instead of running the code block once, they jump back to the "top" where the while is, and repeat, until the expression is False.

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)
    
# one reason why loop is hard to understand is the brain space. Human don't have enough brain power to stimulate the loop visually in their head, hard to go through the process