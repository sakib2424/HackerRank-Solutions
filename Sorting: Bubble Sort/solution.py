#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
def swap(index1, index2, array):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def countSwaps(a):
    # Write your code here
    total_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j+1]):
                total_swaps += 1
                swap(j,j+1,a)
    print("Array is sorted in " + str(total_swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
