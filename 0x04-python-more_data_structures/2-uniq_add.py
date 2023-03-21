#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that adds all unique integers in a list (only once for each integer)"""

def uniq_add(my_list=[]):
    new_list = set(my_list)
    sums = sum(new_list)
    return sums
