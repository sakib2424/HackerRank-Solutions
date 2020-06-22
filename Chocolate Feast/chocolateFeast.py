#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.


def chocolateFeast(n, c, m):
    number_of_chocolates = int(n / c)
    number_of_wrappers = 0
    total_eaten = 0
    while (number_of_chocolates != 0 or number_of_wrappers >= m):
        # The number of wrappers you will collect
        number_of_wrappers += number_of_chocolates
        # Now eat everyting
        total_eaten += number_of_chocolates
        number_of_chocolates = 0
        # Then convert the wrappers to chocolates
        number_of_chocolates = int(number_of_wrappers / m)
        number_of_wrappers = int(number_of_wrappers % m)
    return (total_eaten)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
