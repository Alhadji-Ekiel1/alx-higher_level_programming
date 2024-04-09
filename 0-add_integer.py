#!/usr/bin/python3
"""this Defines our add_integer function."""

def add_integer(a, b=98):
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")


    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a) #convert to interger
    b = int(b) #convert to interger

    return a + b

