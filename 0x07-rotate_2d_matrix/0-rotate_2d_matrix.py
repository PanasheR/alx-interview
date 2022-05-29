#!/usr/bin/python3
"""
Rotate a matrix 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume 2 dimensions and will not be empty.
    Arguments
    ---------
    - matrix  : matrix
                list of non-negative integers.
    Returns
    -------
    - Nothing. The function modifies the original argument
    """

    # a copy of og matrix
    seto = matrix[:]

    for i in range(len(matrix)):

        # i column from the copy
        col_y = [row[i] for row in seto]

        # place it in reverse on og
        matrix[i] = col_y[::-1]
