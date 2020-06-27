#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.

# Passed all test cases


def gridSearch(G, P):
    graph_width = len(G[0])
    graph_height = len(G)
    block_width = len(P[0])
    block_height = len(P)
    # Now iterate from 0 to the last possible firt digit
    # going downard on G
    for i in range(0, graph_height-block_height+1):
        # Then iterate from 0 to the last possible first digit
        # going RIGHTWARD on G
        for j in range(0, graph_width-block_width+1):
            # Helper function to test if there is a match
            if checkMatch(G, P, i, j):
                return "YES"
    return "NO"


def checkMatch(G, P, i, j):
    # We use a double for loop to compare G and P
    for x in range(i, i+len(P)):
        for y in range(j, j+len(P[0])):
            # If at any point there is a number that doesn't
            # match between the graphs we have no match
            if(G[x][y] != P[x-i][y-j]):
                return False
    # If every number matched by the end
    # of the for loop we have a match
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
