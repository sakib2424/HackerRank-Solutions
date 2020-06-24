#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.

# This solution passed all test cases


def workbook(n, k, arr):
    layout = []
    for chapter in arr:
        counter = 1
        while (chapter != 0):
            if chapter >= k:
                layout.append([number for number in range(counter, counter+k)])
                counter += k
                chapter -= k
            else:
                layout.append(
                    [number for number in range(counter, counter+chapter)])
                chapter = 0
    special_problems = 0
    for i in range(0, len(layout)):
        if i+1 in layout[i]:
            special_problems += 1
    return special_problems


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
