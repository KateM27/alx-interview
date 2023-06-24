#!/usr/bin/python3
"""
Module used to rotate a matrix 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Returns Nothing. The function modifies the original argument
    """

    # create a replica of the original matrix
    copy = matrix[:]

    for i in range(len(matrix)):

        # extract the i column from the copy
        col_i = [row[i] for row in copy]

        # place it on the original matrix in reverse order
        matrix[i] = col_i[::-1]
