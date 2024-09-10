#!/usr/bin/python3

def remove_char_at(string, index):
    """Remove the character at the specified index from the string.

    Args:
        string (str): The original string.
        index (int): The index of the character to remove.

    Returns:
        str: The string with the character removed, or the original string if index is negative.
    """
    if index < 0:
        return string
    return string[:index] + string[index + 1:]
