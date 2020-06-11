#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 

def acmTeam(topic):
    current_max = 0
    max_count = 0
    number_of_participants = len(topic)
    length = len(topic[0])
    for i in range(number_of_participants):
        for j in range(i+1, number_of_participants):
            count = 0
            for x in range(0,length):
                if (topic[i][x] == '1' or topic[j][x] == '1'):
                    count += 1
            if (count > current_max):
                current_max = count
                max_count = 1
            elif (current_max == count):
                max_count += 1
    return [current_max, max_count]



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result)


    
