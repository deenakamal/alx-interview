#!/usr/bin/python3
""" pascal_triangle function"""


def pascal_triangle(n):
    """
    Returns list of integer lists representing the Pascal's triangle
    """

    if n <= 0:
        return []

    result = [[1]]

    for row_index in range(1, n):
        current_row = [1]

        for col_index in range(1, row_index):
            left_value = result[row_index - 1][col_index - 1]
            right_value = result[row_index - 1][col_index]
            current_row.append(left_value + right_value)

        current_row.append(1)
        result.append(current_row)

    return result
