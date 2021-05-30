#!/bin/python3

import math
import os
import random
import re
import sys

def isAnagram(string1, string2):
    list1 = list(string1)
    list2 = list(string2)

    if sorted(list1) == sorted(list2):
        return True

    return False

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    total_anagrams = 0
    for index in range(len(s)):
        # Iterate over multiple string lengths 
        for string_length in range(1, len(s)):
            comparison_string = s[index:(index+string_length)]
            ending_index = len(s) - string_length
            for j in range(index+1, ending_index+1):
                secondary_string = s[j: j+string_length]
                if isAnagram(comparison_string, secondary_string):
                    total_anagrams += 1
    print(total_anagrams)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
