#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    efficient_cost = 0
    optimized = False
    white_optimized = False
    if (bc < wc):
        if (bc + z < wc):
            efficient_cost = bc + z
            optimized = True
            white_optimized = True
    elif (bc > wc):
        if (wc + z < bc):
            efficient_cost = wc + z
            optimized = True
    if (optimized):
        if(white_optimized):
            return((b * bc) + (w * efficient_cost))
        else:
            return((b * efficient_cost) + (w * wc))
    else:
        return ((b * bc) + (w * wc))
    
        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)
        
        print(result)
