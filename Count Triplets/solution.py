#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    first_number_banned_set = set()

    total_possibilities = 0

    if r == 1:
        pure = set(arr)
        for number in pure:
            indicies = [index for index, item in enumerate(arr) if item == number]
            total_possibilities += math.comb(len(indicies), 3)
        return total_possibilities 

    for i in range(len(arr) - 3 + 1):
        first_number = arr[i]

        if first_number in first_number_banned_set:
            # print("index ", i) 
            continue

        second_number = first_number * r
        third_number = second_number * r

        second_number_indices = [index for index, item in enumerate(arr[i+1:]) if item == second_number]
        
        if len(second_number_indices) == 0: 
            first_number_banned_set.add(first_number)
            # print("Banned Set ", first_number_banned_set)
            # print("index ", i) 
            continue

        third_number_indices = [index for index, item in enumerate(arr[i+2:]) if item == third_number] 

        if len(third_number_indices) == 0:
            first_number_banned_set.add(first_number)
            # print("Banned Set ", first_number_banned_set)
            # print("index ", i)
            continue
        
        # print(first_number, second_number, third_number, [i], second_number_indices, third_number_indices) 

        total_possibilities += (len(second_number_indices) * len(third_number_indices))
    
    return total_possibilities


# print(countTriplets([1,2,1,3,1], 1))
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()
