#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    string_length = len(s)
    row = math.floor(math.sqrt(string_length))
    column = math.ceil(math.sqrt(string_length))
    if (row*column < string_length):
        row += 1
    matrix = []
    for i in range(0,string_length,column):
        matrix.append(s[i:i+row+1])
    output = ""
    for i in range(column):
        to_add = ""
        for j in range(row):
            if (i > len(matrix[j]) - 1):
                break
            to_add += matrix[j][i]
        output += to_add + " "
    print(matrix)
    return output[:-1]
    

if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)


