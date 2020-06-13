#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # Convert word to a list 
    list_of_chars = list(w)
    # The first step is to find the smallest switch 
    potential_switches = []
    higher_index_of_swtich = None
    for i in reversed(range(len(w))):
        for j in range(i+1, len(w)):
            if (list_of_chars[j] > list_of_chars[i]):
                potential_switches.append([list_of_chars[j], j])
                higher_index_of_swtich = i
        if (potential_switches):
            break
    if (not potential_switches):
        return "no answer"
    else:
        chosen_one = min(potential_switches)
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[chosen_one[1]]
        list_of_chars[chosen_one[1]] = temp
        # Now minimize the string starting from the highest index
        tail_characters = [list_of_chars[i] for i in range(higher_index_of_swtich+1, len(w))]
        tail_characters.sort(reverse=False)
        for i in range(higher_index_of_swtich+1,len(w)):
            list_of_chars[i] = tail_characters[i-higher_index_of_swtich-1]
    return "".join(list_of_chars)






if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)


    


