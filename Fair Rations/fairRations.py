#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
# This solution passed all test cases


def fairRations(B):
    # First, we convert the array into an array
    # of trues and falses
    count = 0
    boolean_array = [True if number % 2 == 0 else False for number in B]
    # We then iterate through the entire array and if
    # an index is false, we change it to true along with the
    # index in front of it
    for i in range(len(boolean_array) - 1):
        if not boolean_array[i]:
            boolean_array[i] = True
            boolean_array[i+1] = not boolean_array[i+1]
            count += 2
    # If the last index after the for loop is run is true,
    # we have our count
    if boolean_array[-1]:
        return(count)
    # If not, there is no answer possible
    else:
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
