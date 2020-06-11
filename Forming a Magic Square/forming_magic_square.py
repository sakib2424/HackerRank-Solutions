#!/bin/python3

import math
import os
import random
import re
import sys

perms = [
    [[8,1,6], [3,5,7], [4,9,2]],
    [[4,3,8], [9,5,1], [2,7,6]],
    [[2,9,4], [7,5,3], [6,1,8]],
    [[6,7,2], [1,5,9], [8,3,4]],
    [[6,1,8], [7,5,3], [2,9,4]],
    [[8,3,4], [1,5,9], [6,7,2]],
    [[4,9,2], [3,5,7], [8,1,6]],
    [[2,7,6], [9,5,1], [4,3,8]]
]
def findMinCost(matrix, compare):
    totalCost = 0
    for i in range(3):
        for j in range(3):
            totalCost += abs(matrix[i][j] - compare[i][j])
    return totalCost

# Complete the formingMagicSquare function below.
def formingMagicSquare(matrix):
    currentMin = findMinCost(matrix, perms[0])
    for i in range (1,8):
        current = findMinCost(matrix, perms[i])
        if (current < currentMin):
            currentMin = current
    return currentMin

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

