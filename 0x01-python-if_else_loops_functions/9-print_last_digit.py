#!/usr/bin/python3
# Author - Awogbemila Tobi
"""a function that prints the last digit of a number"""

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
