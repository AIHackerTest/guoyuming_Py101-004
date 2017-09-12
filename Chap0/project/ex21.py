#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b
    
def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

# you will see words like "dividing, subtracting, multiplying" in the export, because everytime the def add, divide is carried, it exert the print funciton in it
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes, {what}, can you do it by hand?")