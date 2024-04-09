#!/usr/bin/python3
"""
This module defines our `print_square`
Therefore the  function prints a square
"""

def print_square(size):
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
