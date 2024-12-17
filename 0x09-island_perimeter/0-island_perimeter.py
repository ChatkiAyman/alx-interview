#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid of land and water.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A 2D grid where 1 
        represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
