#!/usr/bin/python3
# This script prints the sum of all arguments passed to it.

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    # Initialize the total sum to 0
    total = 0

    # Loop through the arguments (excluding the script name)
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])  # Add each argument to the total sum

    # Print the final total
    print("{}".format(total))
