#!/bin/python3

import math
import os
import random
import re
import sys

num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty'}

# Complete the timeInWords function below.
def timeInWords(h, m):
    possible_status = {0: "o' clock", 15: "quarter", 30: "half", 45: "quarter"}
    if m in possible_status:
        if m==0:
            return (number(h) + " " + possible_status[0]).lower()
        else:
            if m <= 30:
                return (possible_status[m] + " past " + number(h)).lower()
            else:
                return (possible_status[m] + " to " + number(h+1)).lower()
    else:
        if m <= 30:
            if (m == 1):
                return (number(m) + " minute past " + number(h)).lower()
            else:
                return (number(m) + " minutes past " + number(h)).lower()
        else:
            return (number(60-m) + " minutes to " + number(h+1)).lower()



def number(number):
    if (number >= 1) and (number < 19):
        return (num2words1[number])
    elif (number > 20):
        if (number % 10 == 0):
            return (num2words2[number])
        else:
            return (num2words2[int(str(number)[0])] + " " + num2words1[number % 10])
    else:
        print("Number Out Of Range")


if __name__ == '__main__':

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)
