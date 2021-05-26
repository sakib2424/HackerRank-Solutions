#!/bin/python3

import math
import os
import random
import re
import sys

# Will return the optimal achievable value given a remainign value 
def recurseive_func(k, arr, optimal_dic, remaining_value, K_achieved):
    if K_achieved[0]:
        return k
    # Memoize 
    if remaining_value in optimal_dic:
        return optimal_dic[remaining_value]

    possible_solutions = []
    for number in arr:
        subtrated_output = remaining_value - number
        if subtrated_output > 0:
            # Solution if we stop here 
            possible_solutions.append(k-subtrated_output)
            # Solution if we take another option 
            alternate = recurseive_func(k, arr, optimal_dic, subtrated_output, K_achieved)
            if alternate:
                possible_solutions.append(alternate)
        elif subtrated_output == 0:
            K_achieved[0] = True
            optimal_dic[remaining_value] = k
            return k

    if len(possible_solutions) > 0:            
        optimized_solution = max(possible_solutions)
        optimal_dic[remaining_value] = optimized_solution
        return(optimized_solution)
    return None
        
# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    # Stores optimal value from remaining amount 
    optimal_dic = {}
    K_achieved = [False]
    output = recurseive_func(k, arr, optimal_dic, k, K_achieved)
    if output:
        return output
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sys.setrecursionlimit(10**6)
    t = int(input())
    
    for i in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w') 
#     sys.setrecursionlimit(10**6)
#     f = open ("input.txt", "r")

#     t = int(f.readline())
    
#     for i in range(t):
#         nk = f.readline().split()

#         n = int(nk[0])

#         k = int(nk[1])

#         arr = list(map(int, f.readline().rstrip().split()))

#         result = unboundedKnapsack(k, arr)

#         print(str(result) + '\n')
