#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Write your code here
    openings = set(["(", "[", "{"])
    matches = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in s:
        if character in openings:
            stack.append(character)
        elif len(stack) > 0 and matches[character] == stack[-1]:
            stack.pop()
        else:
            return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
    return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
