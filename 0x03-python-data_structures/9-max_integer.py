#!/usr/bin/python3
"""Author: Awogbemila Tobi
Function that returns the maximum value of element in a list"""

def max_integer(my_list=[]):
    
    max_int = 0
    if len(my_list) == 0:
        return None
    else:
        for elements in my_list:
            if elements > max_int:
                max_int = elements
            else:
                continue
    return max_int
            

