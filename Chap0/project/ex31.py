#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

print("""You enter a dark room with two doors.
Do you go through dorr #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating cheese cake.")
    print("What do you do?")
    print("1. Take the cake.\n2. Scream at the bear.")
    
    bear == input("> ")

    if bear == "1":
        print("The bear eats your face off.")
    elif bear == "2":
        print("The bear eats your leg off.")
    else:
        print(f"well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's ret")
    print("1. Blueberries.\n2. Yellow jeacket clothespins.\n3. Understanidng revolvers.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind.")
    else:
        print("The insanity rots your eyes into.")
else:
    print("You stumble around and fall on a knife.")