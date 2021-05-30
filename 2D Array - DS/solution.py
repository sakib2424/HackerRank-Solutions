#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    values = []
    for i in range(len(arr) - 2):
        for start_point in range(len(arr[0]) - 2):
            # Start calculating hour class shape here 
            numbers = []
            # Top Left 
            numbers.append(arr[i][start_point])
            # Top 
            numbers.append(arr[i][start_point+1])
            # Top Right 
            numbers.append(arr[i][start_point+2])
            # Middle 
            numbers.append(arr[i+1][start_point+1])
            # Bottom left 
            numbers.append(arr[i+2][start_point])
            # Bottom 
            numbers.append(arr[i+2][start_point+1])
            # Bottom right 
            numbers.append(arr[i+2][start_point+2])
            sum_for_current_hourglass = sum(numbers)
            values.append(sum_for_current_hourglass)
    return max(values)

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
