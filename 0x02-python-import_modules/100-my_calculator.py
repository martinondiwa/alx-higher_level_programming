#!/usr/bin/python3
# This script handles basic arithmetic operations (addition, subtraction, multiplication, and division)
# using command-line arguments.

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    # Check if the number of arguments is correct
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Define supported operators
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the operator is valid
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Parse the operands and perform the operation
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
