#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.

# This solution passed all test cases


def cavityMap(grid):
    to_delete = []
    # Iterate starting from the second row
    for i in range(1, len(grid)-1):
        # Iterate starting from the second column
        for j in range(1, len(grid[0]) - 1):
            selected = grid[i][j]
            # Comapre the slected cell with its surroundings
            if (selected > grid[i-1][j] and selected > grid[i+1][j] and selected > grid[i][j+1] and selected > grid[i][j-1]):
                # If it is greater than all of them, add it to be X'ed out
                to_delete.append([i, j])
    # Now replace the grid with X's where appropriate
    for pair in to_delete:
        grid[pair[0]] = grid[pair[0]][0:pair[1]] + \
            "X" + grid[pair[0]][pair[1]+1:]
    return grid


if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(result)
