#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def recurse(amount_remaining, current_index, full_list, master_dic): 
    if ((amount_remaining, current_index) in master_dic):
        return master_dic[(amount_remaining, current_index)]

    if amount_remaining == 0:
        return 1

    current_number = full_list[current_index]

    if current_index == len(full_list) - 1:
        if amount_remaining % current_number == 0:
            return 1
        else:
            return 0

    max_possible = amount_remaining // current_number
    total_possibilities = 0

    for i in range(max_possible+1):
        new_amount_remaining = amount_remaining - (i* current_number)
        total_possibilities += recurse(new_amount_remaining, current_index + 1, full_list, master_dic)

    master_dic[(amount_remaining, current_index)] = total_possibilities

    return total_possibilities


def getWays(n, c):
    master_dic = {}

    sorted_arr = sorted(c, reverse=True)

    answer = recurse(n, 0, sorted_arr, master_dic)

    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    f = open("input.txt")

    first_multiple_input = f.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, f.readline().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    # fptr.write(str(ways) + '\n') 
    print(str(ways) + '\n')

    # fptr.close()
