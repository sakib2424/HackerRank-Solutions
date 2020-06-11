#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    dic = {}
    for number in arr:
        if number in dic:
            dic[number] = dic[number] + 1
        else:
            dic[number] = 1
    return (len(arr) - max(dic.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

