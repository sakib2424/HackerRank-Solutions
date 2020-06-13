#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dic = {}
    for index in range(len(a)):
        if a[index] in dic:
            dic[a[index]].append(index)
        else:
            dic[a[index]] = [index]
    filtered_list = [indexes for indexes in dic.values() if len(indexes) > 1]
    current_min = None
    for item in filtered_list:
        for i in range(len(item) - 1):
            difference = item[i+1] - item[i]
            if (current_min == None or current_min > difference):
                current_min = difference
    if (current_min):
        return current_min
    else:
        return -1


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)

