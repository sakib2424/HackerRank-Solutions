#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#
# def recurse(arr, index, max_range, previous_number, final_number):
#     possible_counts = 0
#     final_index_reached = True if index == len(arr) - 2 else False
#     for i in range(max_range+1):
#         if final_index_reached:
#             if i != previous_number and i != final_number:
#                 possible_counts += 1
#         else:
#             if i != previous_number:
#                 possible_counts += 1
#     if final_index_reached:
#         return possible_counts
#     else:
#         return possible_counts * recurse(arr, index+1, max_range, )

def recurse(arr, k, index):
    possible_values = [i for i in range(k) if i != arr[index-1]]
    for possible_value in possible_values:
        arr

def rec(dic_arr, k, index):
    return


def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    dummy_list = [1]
    for i in range(1,n-1):
        dummy_list.append(None)
    dummy_list.append(x)

    recurse(dummy_list, 1, k, 1, x)
    print(dummy_list)

countArray(4, 3, 2)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     x = int(first_multiple_input[2])

#     answer = countArray(n, k, x)

#     fptr.write(str(answer) + '\n')

#     fptr.close()
