#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid.
    Returns:
        int: The perimeter of the island formed by land cells.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Check if the cell is land
                # Add 4 for the current land cell
                perimeter += 4

                # Subtract 1 for each neighboring land cell
                if col + 1 < cols and grid[row][col + 1] == 1:
                    perimeter -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if row + 1 < rows and grid[row + 1][col] == 1:
                    perimeter -= 1
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

    return perimeter
