#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    master = [0]*(n+1)
    for item in queries:
        master[item[0] - 1] += item[2]
        master[item[1]] -= item[2]
    master.pop(-1)
    # counter = master[0]
    # for i in range(1,len(master)):
    #     counter += master[i]
    #     master[i] = counter
    tmp, out = 0, 0
    for num in master:
        tmp += num
        if (tmp > out):
            out = tmp
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

