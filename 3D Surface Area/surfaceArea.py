#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.


def surfaceArea(A):
    total_area = 0
    # Iterate through ever row
    for array in A:
        # Add the area of the base and roof
        for number in array:
            if number > 0:
                total_area += 2
        # Now handle the right hand and left hand sides
        total_area += array[-1]
        total_area += array[0]
    # Now handle the top side
    for number in A[0]:
        total_area += number
    # And here handle the bottom side
    for number in A[-1]:
        total_area += number
    # Here we iterate through every block in the
    # matrix and add the difference in height between that unit
    # and its surrounding blocks
    for i in range(len(A)):
        for j in range(len(A[0])):
            current_spot = A[i][j]
            # This if statement handles blocks that are in the center of the matrix
            if (i != 0 and i != len(A) - 1 and j != 0 and j != len(A[0]) - 1):
                total_area = addSides(
                    ["up", "down", "left", "right"], total_area, i, j, A)
            # This statement handles cases of the corner blocks
            # or the first and last rows/columns of the shape
            else:
                if (i == 0):
                    if(j == 0):
                        total_area = addSides(
                            purify(["down", "right"], i, j, A), total_area, i, j, A)
                    elif(j == len(A[0]) - 1):
                        total_area = addSides(
                            purify(["down", "left"], i, j, A), total_area, i, j, A)
                    else:
                        total_area = addSides(
                            purify(["down", "left", "right"], i, j, A), total_area, i, j, A)
                elif (i == len(A) - 1):
                    if(j == 0):
                        total_area = addSides(
                            purify(["up", "right"], i, j, A), total_area, i, j, A)
                    elif(j == len(A[0]) - 1):
                        total_area = addSides(
                            purify(["up", "left"], i, j, A), total_area, i, j, A)
                    else:
                        total_area = addSides(
                            purify(["up", "left", "right"], i, j, A), total_area, i, j, A)
                elif (j == 0):
                    # We don't have to worry about the edge cases
                    # Just handle the middle case
                    total_area = addSides(
                        purify(["up", "down", "right"], i, j, A), total_area, i, j, A)
                elif (j == len(A[0]) - 1):
                    # We don't have to worry about the edge cases
                    # Just handle the middle case
                    total_area = addSides(
                        purify(["up", "down", "left"], i, j, A), total_area, i, j, A)
    return total_area


# This purify statement removes invalid comparisons between
# cells when there is only one row or column in the matrix
def purify(normal_array, i, j, A):
    height = len(A)
    width = len(A[0])
    if height == 1:
        if "down" in normal_array:
            normal_array.remove("down")
        if "up" in normal_array:
            normal_array.remove("up")
    if width == 1:
        if "left" in normal_array:
            normal_array.remove("left")
        if "right" in normal_array:
            normal_array.remove("right")
    return normal_array


# Given an array of the valid comparisons, this
# function adds the difference in height between
# a cell and all of its shorter neighbors
def addSides(sides_to_add, total_area, i, j, A):
    current = A[i][j]
    if "up" in sides_to_add:
        if (current > A[i-1][j]):
            total_area += current - A[i-1][j]
    if "down" in sides_to_add:
        if (current > A[i+1][j]):
            total_area += current - A[i+1][j]
    if "left" in sides_to_add:
        if (current > A[i][j-1]):
            total_area += current - A[i][j-1]
    if "right" in sides_to_add:
        if (current > A[i][j+1]):
            total_area += current - A[i][j+1]
    return total_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
