#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Given an nxn 2D matrix, rotate it 90 degrees clockwise
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_2d_matrix(matrix)
print(matrix)
