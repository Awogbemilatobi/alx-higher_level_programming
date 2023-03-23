#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that prints a matrix of integers"""

def print_matrix_integer(matrix=[[]]):
        for column in matrix:
            print()
            for line in column:
                print(f"{str(line)} ", end='')
        print()




