#!/usr/bin/python3
"""Author: Awogbemila tobi
a function that returns a list with all values multiplied by a
number without using any loops."""

def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda num: num*number, my_list))
    return new_list
