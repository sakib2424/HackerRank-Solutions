#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def recurse(arr, index, total_sum, prev_value, master_dic):
    # flag = True if index == len(arr) - 1 else False

    if (index, total_sum) in master_dic:
        return master_dic[(index, total_sum)]

    if index == len(arr):
        return total_sum

    possible_sums = []
    for possible_value in range(1, arr[index]+1):
        if index == 0:
            possible_sums.append(recurse(arr, index+1, total_sum, possible_value, master_dic))
        else:
            possible_difference = abs(possible_value - prev_value)
            new_total = total_sum + possible_difference
            possible_sums.append(recurse(arr, index+1, new_total, possible_value,master_dic))
    
    answer = max(possible_sums)
    master_dic[(index, total_sum)] = answer

    # if flag:    
    #     print(possible_value, possible_sums)

    return max(possible_sums) 
        


def cost(B):
    # Write your code here
    master_dic = {}
    print(recurse(B, 0, 0, None, master_dic))

cost([10,1,10,1,10]) 
# cost([1,2,3])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         B = list(map(int, input().rstrip().split()))

#         result = cost(B)

#         fptr.write(str(result) + '\n')

#     fptr.close()
