#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

# read a file as argv
def print_all(f):
    print(f.read())

# seek the first place in the file?
def rewind(f):
    f.seek(0)
    
# count and read a line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# set a file to open, unpacking the variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)