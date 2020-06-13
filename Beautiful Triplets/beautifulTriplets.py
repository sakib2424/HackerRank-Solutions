#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    solution = []
    output = []
    # Correct and passes all test cases 
    return non_recursive_solution(d,arr)
    # Correct but does not execute within limits for test cases 
    # recursive_solution(arr, d, solution, 0, output)
    # return (len(output)) 

# Best soltion, passes cases 
def non_recursive_solution(d, arr):
    count = 0
    for i in range(len(arr) - 2):
            for j in range(i+1, len(arr) - 1):
                target = arr[i] + d
                if (arr[j] == target):
                    target2 = arr[j] + d
                    for z in range(j+1, len(arr)):
                        if(arr[z] == target2):
                            count += 1
    return count

# Working solution, does not pass cases though 

def recursive_solution(arr, d, solution, position, output):
    if (position == len(arr)):
        if (len(solution) == 3):
            output.append(solution)
    elif (len(solution) == 3):
        output.append(solution)
    elif (not solution):
        # Without adding the number
        recursive_solution(arr, d, copy.deepcopy(solution), position+1, output)
        # With adding number
        deep_copy = copy.deepcopy(solution)
        deep_copy.append(arr[position])
        recursive_solution(arr, d, deep_copy, position+1, output)
    else:
        # The current number satisfies the difference 
        if (arr[position] - solution[-1] == d):
            # Do it without the number 
            recursive_solution(arr, d, copy.deepcopy(solution), position+1, output)
            # And then do it with the number
            deep_copy = copy.deepcopy(solution)
            deep_copy.append(arr[position])
            recursive_solution(arr, d, deep_copy, position+1, output)
        # If it doesn't satisify the difference we move on to the next position 
        else:
            recursive_solution(arr, d, copy.deepcopy(solution), position+1, output)



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)


