#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 
from itertools import permutations 

def organizingContainers(container):
    side = len(container)
    bucket_totals = [sum(bucket) for bucket in container]
    type_totals = [sum([bucket[i] for bucket in container]) for i in range(side)]
    while(len(bucket_totals) > 0):
        to_match = bucket_totals[0]
        if (to_match in type_totals):
            type_totals.remove(to_match)
            bucket_totals.remove(to_match)
        else:
            break
    if (len(bucket_totals) > 0):
        return "Impossible"
    else:
        return "Possible"      

if __name__ == '__main__':
    f = open("input.txt", "r")
    q = int(f.readline())

    for q_itr in range(q):
        n = int(f.readline())
        container = []
        for _ in range(n):
            container.append(list(map(int, f.readline().rstrip().split())))
        result = organizingContainers(container)
        print(result)
    
    f.close()



    
    
