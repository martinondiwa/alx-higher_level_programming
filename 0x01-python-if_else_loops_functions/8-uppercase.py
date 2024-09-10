#!/usr/bin/python3

def uppercase(str):
    """
    Converts all lowercase letters in a string to uppercase.
    
    Args:
        str: The input string.
    """
    for i in str:
        # Check if the character is lowercase (between 'a' and 'z')
        if ord("a") <= ord(i) <= ord("z"):
            # Convert lowercase letter to uppercase by adjusting the ASCII value
            i = chr(ord(i) - 32)
        # Print the character without a newline and continue
        print("{:s}".format(i), end="")
    
    # Print a newline after the loop finishes
    print()
