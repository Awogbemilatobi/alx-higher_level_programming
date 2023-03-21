#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that computes the square value of all integers of a matrix using map"""

def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
    return new_matrix
