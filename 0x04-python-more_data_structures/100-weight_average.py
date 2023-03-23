#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that returns the weighted average of all
integers tuple (<score>, <weight>)"""

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sums_mul = 0
    sums_div = 0

    for tup in my_list:
        sums_mul += tup[0] * tup[1]
        sums_div += tup[1]

    return (sums_mul / sums_div)
