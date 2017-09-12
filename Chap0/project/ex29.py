#!/usr/bin/env python3
# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats: # if statement tries a Boolean operation, does it evaluate true?
    print("Too many cats! The world is doomed!") # indented because it exerts only if "if" requirement is met 

if people > cats:
    print("Not many cats! The world is saved.")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry.")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs!")

if people == dogs:
    print("People are dogs.")