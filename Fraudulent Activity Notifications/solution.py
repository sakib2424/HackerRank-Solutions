#!/bin/python3

import math
import os
import random
import re
import sys

import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    total_notifications = 0
    odd = d % 2 == 1
    sorted_arr = None
    for i in range(d, len(expenditure)):
        if i == d:
            sorted_arr = sorted(expenditure[i - d : i])
        else:
            # Remove trailing number 
            number_to_remove = expenditure[i - d - 1]
            index_of_removal = bisect.bisect_left(sorted_arr, number_to_remove)
            sorted_arr.pop(index_of_removal)
            # Insert new element 
            bisect.insort(sorted_arr, expenditure[i-1])
        if odd:
            median = sorted_arr[d // 2]
        else:
            second_index = d // 2
            first_index = second_index - 1

            median = (sorted_arr[first_index] + sorted_arr[second_index]) / 2
        
        if expenditure[i] >= (2 * median):
            total_notifications += 1

    return total_notifications 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
