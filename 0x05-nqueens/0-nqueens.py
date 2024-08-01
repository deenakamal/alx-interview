#!/usr/bin/python3
"""Defines the N-Queens solver module"""

import sys


def nqueens(n):
    """Solves the N-Queens problem for a board of size n."""
    solutions = []
    cols = []
    find_solutions(n, 0, cols, solutions)
    return solutions


def find_solutions(n, row, cols, solutions):
    """Recursively finds valid queen placements."""
    if row == n:
        solution = []
        for r in range(len(cols)):
            solution.append([r, cols[r]])

        solutions.append(solution)
    else:
        for c in range(n):
            cols.append(c)
            if is_valid(cols):
                find_solutions(n, row + 1, cols, solutions)

            cols.pop()


def is_valid(cols):
    """Checks if the current queen placements are valid."""
    r = len(cols) - 1
    for i in range(r):
        diff = abs(cols[i] - cols[r])
        if diff == 0 or diff == r - i:
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    n = sys.argv[1]

    if not n.isdigit():
        print('N must be a number')
        sys.exit(1)

    if int(n) < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = nqueens(int(n))

    for solution in solutions:
        print(solution)
