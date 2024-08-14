#!/usr/bin/python3
"""
Module
"""


def rotate_2d_matrix(matrix):
    """rotate matrix 90 degrees clockwise"""
    matrix_size = len(matrix)

    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in range(matrix_size):
        matrix[row].reverse()
