#!/bin/python3

import math
import os
import random
import re
import sys

# Returns new array and whether or not all values are the same 
def generate_arr(prev_arr):
    new_arr = []
    all_values_same = True
    for i in range(len(prev_arr)-1):
        number_to_append = None
        if prev_arr[i] < prev_arr[i+1]:
            number_to_append = prev_arr[i]
        else:
            number_to_append = prev_arr[i+1]
        if all_values_same:
            if len(new_arr) > 0 and number_to_append != new_arr[-1]:
                all_values_same = False
        new_arr.append(number_to_append)
    return new_arr, all_values_same

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    output = []
    min_arrays = [arr]

    output.append(max(min_arrays[0]))

    values_converged = False
    convergance_location = None
    terminal_value = None

    for window_size in range(2, len(arr)+1):
        new_arr, all_values_same = generate_arr(min_arrays[-1])

        if all_values_same:
            values_converged = True
            convergance_location = window_size
            terminal_value = new_arr[0]
            break
        else: 
            if (output[window_size-2] in new_arr):
                output.append(output[window_size-2])
            else:
                output.append(max(new_arr))
            min_arrays.append(new_arr)
    
    for x in range(convergance_location, len(arr)+1):
        output.append(terminal_value)

    print(output)


# riddle([1,2,3,5,1,13,3]) 
# riddle([2,6,1,12])
riddle([3,5,4,7,6,2])
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     res = riddle(arr)

#     fptr.write(' '.join(map(str, res)))
#     fptr.write('\n')

#     fptr.close()
