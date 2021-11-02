#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    dic = {}

    for letter in s:
        if letter in dic:
            dic[letter] = dic[letter] + 1
        else:
            dic[letter] = 1
    
    frequencies = [dic[key] for key in dic]

    frequency_of_frequencies = {}

    for freq in frequencies:
        if freq in frequency_of_frequencies:
            frequency_of_frequencies[freq] = frequency_of_frequencies[freq] + 1
        else:
            frequency_of_frequencies[freq] = 1
    if len(frequency_of_frequencies) == 1:
        return "YES"
    elif len(frequency_of_frequencies) == 2:
        if 1 in frequency_of_frequencies and frequency_of_frequencies[1] == 1:
            return "YES"
        keys = [key for key in frequency_of_frequencies]
        if keys[0] > keys[1]:
            greater_freq = keys[0]
            lesser_freq = keys[1]
        else :
            greater_freq = keys[1]
            lesser_freq = keys[0]

        if greater_freq == lesser_freq + 1 and frequency_of_frequencies[greater_freq] == 1:
            return "YES"
        else:
            return "NO"
    return "NO"
        




    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
