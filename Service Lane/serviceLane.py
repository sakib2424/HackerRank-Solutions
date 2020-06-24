#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.

# The original problem had an error, the
# variable "width" was not passed in as
# a parameter to the function

# This solution passes all test cases


def serviceLane(n, cases, width):
    output = []
    for case in cases:
        output.append(min(width[case[0]:case[1] + 1]))
    return output


if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)
