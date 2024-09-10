#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Perform a calculation based on the values of a, b, and c.

    Args:
        a (int or float): The first parameter.
        b (int or float): The second parameter.
        c (int or float): The third parameter.

    Returns:
        int or float: The result of the calculation based on the conditions.
    """
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c
