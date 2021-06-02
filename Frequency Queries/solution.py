#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    master_dic = {}
    output = []
    frequency_dic = {}
    for q in queries:
        query_type = q[0]
        query_target = q[1]

        if query_type == 1:
            current_retrieved_value = master_dic.get(query_target, 0)
            # Remove old value 
            frequency_dic[current_retrieved_value] = frequency_dic.get(current_retrieved_value, 1) - 1
            # Increment the frequency 
            new_value = current_retrieved_value + 1
            master_dic[query_target] = new_value
            # Add new value 
            frequency_dic[new_value] = frequency_dic.get(new_value, 0) + 1

        elif query_type == 2:
            current_retrieved_value = master_dic.get(query_target, 0)
            # Remove old value 
            frequency_dic[current_retrieved_value] = frequency_dic.get(current_retrieved_value, 1) - 1
            # Decrement the frequency
            new_value = current_retrieved_value - 1 if current_retrieved_value - 1 >= 0 else 0
            master_dic[query_target] = new_value 
            # Add new value 
            frequency_dic[new_value] = frequency_dic.get(new_value, 0) + 1
        else:
            if query_target in frequency_dic and frequency_dic[query_target] != 0:
                output.append(1)
            else:
                output.append(0)
    return output
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
