#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    master_array = []
    last_answer = 0
    last_numbers = []
    for x in range(n):
        master_array.append([])
    for array in queries:
        selected = (array[1] ^ last_answer) % n
        if array[0] == 1:
            master_array[selected].append(array[2])
        else:
            value = array[2] % master_array[selected].__len__() 
            last_answer = master_array[selected][value]
            last_numbers.append(last_answer)
            print(last_answer)
    return last_numbers
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

