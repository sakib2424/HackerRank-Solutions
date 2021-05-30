#!/bin/python3

import math
import os
import random
import re
import sys

def swap(position1, position2, array):
    temp = array[position1]
    array[position1] = array[position2]
    array[position2] = temp

def swap_dic(number1, number2, dic):
    temp = dic[number1]
    dic[number1] = dic[number2]
    dic[number2] = temp

def minimumSwaps(arr):
    total_swaps = 0
    # Maps the number to its index 
    mapping_dic = {}
    for index in range(len(arr)):
        mapping_dic[arr[index]] = index

    for index in range(len(arr) - 1):
        right_number = index + 1
        if arr[index] != right_number: 
            # correct_location = arr.index(index+1, index+1, len(arr)) 
            correct_location = mapping_dic[index + 1]

            # For the dictionary swapping 
            number_at_correct_location = arr[correct_location]
            this_number = arr[index]
            # Swaps array 
            swap(index, correct_location, arr)
            # Swap dictionary 
            swap_dic(number_at_correct_location, this_number, mapping_dic)

            total_swaps += 1

    return total_swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
