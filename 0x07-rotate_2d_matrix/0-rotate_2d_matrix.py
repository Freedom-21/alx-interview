#!/usr/bin/python3
"""2D matrix rotation module."""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    colums = len(matrix[0])
    if not all(map(lambda x: len(x) == colums, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(colums * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == colums - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
