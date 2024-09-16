#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from a string.

    Args:
        my_string (str): The string from which 'c' and 'C' are to be removed.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    return ''.join([char for char in my_string if char.lower() != 'c'])
