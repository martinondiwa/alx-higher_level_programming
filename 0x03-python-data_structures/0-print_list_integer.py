#!/usr/bin/python3

def print_list_integer(my_list=None):
    """
    Prints all integers in a list, each followed by a newline.

    Args:
        my_list (list): A list of integers. Defaults to None.
    """
    if my_list is None:
        my_list = []

    for i in my_list:
        print("{:d}".format(i))
