#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def swap(first_index, second_index, array):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp

def minimumBribes(q):
    # Check if any person is too far ahead 
    for index in range(len(q)):
        original_position = q[index]
        current_position = index + 1
        if current_position < original_position - 2:
            print("Too chaotic")
            return

    total_number_of_swaps = 0
    all_sorted = False
    starting_point = 0
    while(not all_sorted):
        # Find first misplaced number 
        misplaced_found = False
        for index in range(starting_point, len(q) - 1):
            if q[index] > q[index+1]:
                swap(index, index+1, q)
                total_number_of_swaps += 1
                misplaced_found = True
                if (index - 1 < 0):
                    starting_point = 0
                else:
                    starting_point = index - 1
                break
        if not misplaced_found:    
            all_sorted = True
        
    print(total_number_of_swaps)
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
