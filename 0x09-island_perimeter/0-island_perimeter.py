#!/usr/bin/python3
def island_perimeter(grid):

    """
    Calculates the perimeter of the island described in the grid.

    The grid is a 2D list where:
    - 0 represents water
    - 1 represents land

    Each land cell contributes to the perimeter based on its exposure to water or the grid boundary.

    Args:
    grid (list of list of int): A 2D grid representing the map. Each cell is either 0 (water) or 1 (land).

    Returns:
    int: The perimeter of the island described by the grid.

    Example:
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12

    This function assumes:
    - The grid is rectangular with at least one land cell (1).
    - The grid is completely surrounded by water (0).
    - There is only one island (or no land at all).
    """


    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # If it's land
                # Check the four sides of the cell
                if i == 0 or grid[i - 1][j] == 0:  # North
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # South
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # West
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # East
                    perimeter += 1

    return perimeter
