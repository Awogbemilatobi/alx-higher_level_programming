#!/usr/bin/python3
#Author: Awogbemila Tobi

"""Define a class Square."""


class Square:
    """Represent a square if its an integer whose value
        is greater than than or equal to zero."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
