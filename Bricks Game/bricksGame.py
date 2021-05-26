#!/bin/python3

import os
import sys

#
# Complete the bricksGame function below.
#
def bricksGame(arr):
    starting_position = 0
    starting_score = 0
    optimals_from_positions = {}
    output = bricksGame(arr, 0, starting_score, optimals_from_positions, len(arr))

def recursive_sol(arr, position, score, optimals_from_positions, arr_length):
    if position in optimals_from_positions:
        return optimals_from_positions[position]
    
    option_range = min(3, arr_length - position)

    possible_outcomes = []

    for i in range(option_range):
        break
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
