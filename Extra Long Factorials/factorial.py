#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    master_list = []
    for i in str(n):
        master_list.insert(0,int(i))
    
    for number in range(1,n):
        carry = 0
        for place in range(len(master_list)):
            total = number*master_list[place] + carry
            master_list[place] = int(str(total)[-1])
            if (total > 9):
                carry = int(str(total)[0:len(str(total)) - 1])
            else:
                carry = 0
        # Now append from carry 
        for digit in reversed(str(carry)):
            master_list.append(int(digit))
    
    string_form = reversed([str(digit) for digit in master_list])
    final = "".join(string_form)

    while (final[0] == "0"):
        final = final[1:len(final)]

    return(final)
        

if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)
    # for i in range(5,1,-1):
    #     print(i)