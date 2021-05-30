#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    master = [0]*(n+1)

    for query in queries:
        starting_index = query[0] - 1
        ending_index = query[1] - 1
        number_to_add = query[2] 

        master[starting_index] += number_to_add
        master[ending_index+1] -= number_to_add
    
    highest_number = master[0]
    current = master[0]
    for index in range(1, len(master)):
        current += master[index]
        if current > highest_number:
            highest_number = current
    
    return highest_number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

