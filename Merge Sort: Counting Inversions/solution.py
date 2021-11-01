#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    sorted_array = sorted(arr)
    index_mapping = {}
    for index in range(len(sorted_array)):
        number_at_hand = sorted_array[index]
        if number_at_hand in index_mapping:
            index_mapping[number_at_hand].add(index)
        else:
            index_mapping[number_at_hand] = set()
            index_mapping[number_at_hand].add(index)

    # Now generate misplacements index
    misplaced_index = []
    for index in range(len(arr)):
        number = arr[index]
        possible_differentials = [index - possible_valid_index for possible_valid_index in index_mapping[number]]
        differential = min(possible_differentials, key=abs)
        misplaced_index.append(differential)

    print(misplaced_index)

    # sorting_complete = False

    # while (not sorting_complete):
    #     # identify max and min misplacements 
    #     for 

def swap(index1, index2, array):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def countSwaps(a):
    # Write your code here
    total_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j+1]):
                total_swaps += 1
                swap(j,j+1,a)
    print("Array is sorted in " + str(total_swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

countSwaps([2, 1, 3, 1, 2])        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         arr = list(map(int, input().rstrip().split()))

#         result = countInversions(arr)

#         fptr.write(str(result) + '\n')

#     fptr.close()
