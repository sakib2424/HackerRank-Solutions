#!/bin/python3
import math
import os
import random
import re
import sys
import itertools
from itertools import product
import copy

# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    sol = [[], None]
    # Dictionary to store recursive solutions 
    starting_points = {}
    # This calls the optimized solition
    return best_solution(k,s)
    # Dictionary to store recursive solutions 
    starting_points = {}
    # This calls recursive solution (also works, but doesn't pass test cases)
    return recursive_solution(k,s,[],0)

# This is the solution that passed hackerrank 
def best_solution(k,s):
    buckets = [[] for i in range(k)]
    for number in s:
        buckets[number % k].append(number)
    count = 0
    # Take one from the zero bucket 
    if (len(buckets[0]) > 0):
        count += 1
    if (k == 1):
        return count
    # If there are an even number of bucekts
    if (k == 2):
        if (len(buckets[1]) > 1):
            count += 1
        return count
    if (k % 2 == 0):
        for i in range(1, int(k / 2)):
            if(len(buckets[i]) > len(buckets[k-i])):
                count += len(buckets[i])
            else:
                count += len(buckets[k-i])
        if (len(buckets[int(k/2)]) > 0):
            count += 1
     # If there are an odd number of bucekts
    else:
        for i in range(1, int(k/2) + 1):
            if(len(buckets[i]) > len(buckets[k-i])):
                count += len(buckets[i])
            else:
                count += len(buckets[k-i])
    return(count)


# Sol is the array and the starting point of the array 
def recursive_solution(k, s, sol, index, starting_points):
    if (sol[1] in starting_points.keys()):
        return starting_points[sol[1]]
    if (index == len(s)):
        if (sol is None):
            return 0
        else:
            return len(sol[0])
    if (check_compatible_digit(sol[0], s[index], k)):
        if (sol is None):
            with_number = recursive_solution(k, s, [[s[index]], index], index+1, starting_points)
        elif (len(sol) == 0):
            with_number = recursive_solution(k, s, [[s[index]], index], index+1, starting_points)
        else:
            deep_copy = copy.deepcopy(sol)
            deep_copy[0].append(s[index])
            with_number = recursive_solution(k, s, deep_copy, index+1, starting_points)
        without_number = recursive_solution(k,s, sol, index+1, starting_points)
        maximum  = max(with_number, without_number)
        starting_points[sol[1]] = maximum
        return maximum
    else:
        return recursive_solution(k,s, sol, index+1, starting_points)

def check_compatible_digit(array, new, k):
    if array is None:
        return True
    for item in array:
        if ((item + new) % k == 0):
            return False
    return True

if __name__ == '__main__':
    f = open("input3.txt", "r")
    kay = int(f.readline().split(" ")[1])
    input_array_string = f.readline().split(" ")
    input_array = [int(s) for s in input_array_string]
    f.close()
    # Call the function
    # print(nonDivisibleSubset(kay, input_array))
    print(best_solution(kay,input_array))


