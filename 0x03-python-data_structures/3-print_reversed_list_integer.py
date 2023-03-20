#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that prints all integers of a list, in reverse order"""

def print_reversed_list_integer(my_list=[]):
    for line in reversed(my_list):
        print(f"{str(line)}")
