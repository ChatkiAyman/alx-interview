#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid of land and water.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # If it's land
                # Check the four sides of the land cell
                if i == 0 or grid[i - 1][j] == 0:  # North (top side)
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # South (bottom side)
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # West (left side)
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # East (right side)
                    perimeter += 1

    return perimeter
