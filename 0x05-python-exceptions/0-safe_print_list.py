#!/usr/bin/python3
#Author: Awogbemila Tobi

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    num = 0
    for elements in range(x):
        try:
            print(my_list[elements], end='')
            num = num + 1
        except IndexError:
            break
    print()
    return num
