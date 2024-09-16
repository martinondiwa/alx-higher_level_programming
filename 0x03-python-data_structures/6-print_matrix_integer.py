#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists of int): The matrix to be printed.
    """
    if matrix is None or not matrix:
        print()
        return
    
    for row in matrix:
        print(" ".join("{:d}".format(item) for item in row))
