#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specified index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace the element.
        element (any): The new element to insert into the list.

    Returns:
        list: The modified list if the index is valid; otherwise, the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
