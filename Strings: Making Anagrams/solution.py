#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_dic = {}
    b_dic = {}

    # Populate a 
    for letter in a :
        if letter in a_dic: 
            a_dic[letter] = a_dic[letter] + 1
        else:
            a_dic[letter] = 1

    # Populate b 
    for letter in b :
        if letter in b_dic: 
            b_dic[letter] = b_dic[letter] + 1
        else:
            b_dic[letter] = 1
    
    total_subtractions = 0

    for letter in a_dic:
        # Handle case where both strings have the letter 
        if letter in b_dic:
            to_add = abs(a_dic[letter] - b_dic[letter])
            total_subtractions += to_add
        else:
            total_subtractions += a_dic[letter]
    
    for letter in b_dic:
        if letter not in a_dic:
            total_subtractions += b_dic[letter]

    return total_subtractions

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

