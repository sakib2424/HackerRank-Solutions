#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def find_area(min_index, array):
    current_height = array[min_index]
    spread = 1
    # Expand left 
    for i in range(min_index-1, -1, -1):
        if current_height <= array[i]:
            spread += 1
        else: 
            break
    # Expand right 
    for i in range(min_index+1, len(array)):
        if current_height <= array[i]:
            spread += 1
        else:
            break
    return current_height * spread

def largestRectangle(h):
    # Write your code here
    possible_areas = []

    for index in range(len(h)):
        area = find_area(index, h)
        possible_areas.append(area)

    return max(possible_areas)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
