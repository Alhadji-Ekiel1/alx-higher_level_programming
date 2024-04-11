#!/usr/bin/python3
"""Defines an add_integer function."""

def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a (int or float): 1st Number.
        b (int or float, optional): 2nd number. Defaults at 98.

    Returns:
        int(interger): The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
