#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.

# This solution passed all test cases


def flatlandSpaceStations(n, c):
    c = sorted(c)
    distances = []
    # If there is only one stop, calculate the distance,
    # from that stop to all other cities
    if (len(c) == 1):
        index = c[0]
        for i in range(n):
            distances.append(abs(index-i))
    # Or else calculate the distances in between every two rest stops
    else:
        # First handle all values before the first station
        for i in range(0, c[0]):
            distances.append(c[0] - i)
        # This for loop goes over all the stops and calcualtes
        # the distances in between
        for i in range(1, len(c)):
            j = i-1
            if(c[j] + 1 == c[i]):
                distances.append(0)
                continue
            pointer = c[j]
            if ((c[i] - c[j]) % 2 == 0):
                middle = int((c[i] + c[j]) / 2)
                while (pointer <= middle):
                    distances.append(pointer - c[j])
                    pointer += 1
                while (pointer <= c[i]):
                    distances.append(c[i] - pointer)
                    pointer += 1
            else:
                while (pointer <= (c[j] + c[i]) / 2):
                    distances.append(pointer - c[j])
                    pointer += 1
                while (pointer <= c[i]):
                    distances.append(c[i] - pointer)
                    pointer += 1
        # Now handle the values after the last stop
        for i in range(c[-1] + 1, n):
            distances.append(i - c[-1])
    # print(distances)
    return(max(distances))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
