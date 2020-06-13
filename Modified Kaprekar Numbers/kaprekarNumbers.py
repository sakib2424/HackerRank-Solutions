#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    output = []
    for i in range (p,q+1):
        if (i <= 10):
            if (i==1 or i==9):
                output.append(i)
            continue
        string_form = str(i)
        d = len(string_form)
        squared = str(i*i)
        if(len(squared) % 2 == 0):
            right = int(squared[d:])
            left = int(squared[:d])
        else:
            right = int(squared[len(squared) - d:])
            left = int(squared[:d-1])
        if (i == left + right):
            output.append(i)
    if (not output):
        print("INVALID RANGE")
    else:
        print (" ".join([str(x) for x in output]))

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
