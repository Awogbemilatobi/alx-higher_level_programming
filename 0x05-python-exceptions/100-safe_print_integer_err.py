#!/usr/bin/python3
#Author: Awogbemila Tobi

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        """sys.exc_info returns a 3 tuple with the exception, the exceptions parameter
        and a traceback object that pinpoints the line of python that raised the exception"""
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
