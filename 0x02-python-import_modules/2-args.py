#!/usr/bin/python3
# This script prints the number of and list of arguments passed to it.

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Get the number of arguments (excluding the script name)
    count = len(sys.argv) - 1

    # Handle different cases based on the number of arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Loop through the arguments and print each one
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
