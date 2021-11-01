#!/bin/python3

import math
import os
import random
import re
import sys

def swap(index1, index2, array):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def update_differential(index, arr, index_mapping, misplaced_index):
    number_at_index = arr[index]
    possible_differentials = [index - possible_valid_index for possible_valid_index in index_mapping[number_at_index]]
    differential = min(possible_differentials, key=abs)
    misplaced_index[index] = differential


def calculate_new_differntial(index, new_number_at_index, index_mapping, misplaced_index):
    possible_differentials = [index - possible_valid_index for possible_valid_index in index_mapping[new_number_at_index]]
    new_differential = min(possible_differentials, key=abs)
    return new_differential 

def find_swapable_index(arr, index_mapping, misplaced_index):
    swapable = []
    for i in range(len(misplaced_index)):
        if misplaced_index[i] < 0:
            for j in range(i+1, len(misplaced_index)):
                if misplaced_index[j] > 0:
                    # Calcualte current absolute value 
                    current_absolute_value = abs(misplaced_index[i]) + abs(misplaced_index[j])

                    new_left_value = calculate_new_differntial(i, arr[j], index_mapping, misplaced_index)
                    new_right_value = calculate_new_differntial(j, arr[i], index_mapping, misplaced_index)

                    new_absolute_value = abs(new_left_value) + abs(new_right_value)

                    improvement = current_absolute_value - new_absolute_value

                    swapable.append((improvement, (i,j)))
    if len(swapable) == 0:
        return None

    best_swap = max(swapable, key = lambda x: x[0])

    return best_swap[1]

def minimumSwaps(arr):
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
    misplaced_index = [None for item in arr]
    for index in range(len(arr)):
        update_differential(index, arr, index_mapping, misplaced_index)

    sorting_complete = False
    total_swaps = 0

    while (not sorting_complete):
        indicies_to_swap = find_swapable_index(arr, index_mapping, misplaced_index)

        if indicies_to_swap == None:
            sorting_complete= True
            continue

        index_i, index_j = indicies_to_swap

        # Now swap positons of the min and max 
        swap(index_i, index_j, arr)

        # Increment swap coutner 
        total_swaps += 1

        # Now re-calculate the differential array
        update_differential(index_i, arr, index_mapping, misplaced_index)
        update_differential(index_j, arr, index_mapping, misplaced_index)

    print(arr)
    return total_swaps


# print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
# print(minimumSwaps([2,1,3,4,5,6,7])) 
# print(minimumSwaps([1,1,1,2,2]))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()

