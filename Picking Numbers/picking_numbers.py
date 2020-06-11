#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(array):
    # Write your code here
    max_count = 0
    array.sort()
    position = 0
    # current = array[position]
    completed = set()
    # Iterate
    while(position < len(array)):
        if (array[position] in completed):
            position += 1
            continue
        completed.add(array[position])
        # This is the counter 
        back_counter = 1
        # Check backwards
        backPosition = position - 1
        while (backPosition > 0 and (array[position] - array[backPosition]) <= 1):
            back_counter += 1
            backPosition -= 1
        # Check foorwards 
        front_counter = 1
        frontPosition = position + 1
        while (frontPosition < len(array) and (array[frontPosition] - array[position]) <= 1):
            front_counter += 1
            frontPosition += 1
        if (max(front_counter, back_counter) > max_count):
            max_count = max(front_counter, back_counter)
        position += 1
    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
