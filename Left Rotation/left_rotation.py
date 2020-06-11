#!/bin/python3

import math
import os
import random
import re
import sys

def shift(array, d, n):
    if (len(array) < 2):
        return array
    saved = []
    for k in range(d):
        saved.append(array[-(k+1)])
    saved.reverse()
    for i in range(n-d):
        array[i-d] = array[i]
    counter = 0
    for x in range(n-d, n):
        array[x - d] = saved[counter]
        counter += 1
    # first = array[0]
    # for i in range(1,len(array)):
    #     array[i-1] = array[i]
    # array[-1] = first
    # return array

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    d = d % n
    shift(a, d, n)
    for number in a:
        print("%d " % (number), end = '')

