#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    set_of_obstacles = {}
    for obstacle in obstacles:
        set_of_obstacles[str(obstacle)] = 1
    counter = 0
    # Check up 
    for i in range(c_q+1, n+1):
        if (str([r_q,i]) not in set_of_obstacles):
            counter += 1
        else:
            break
    # Check down 
    for i in range(c_q-1, 0, -1):
        if (str([r_q,i]) not in set_of_obstacles):
            counter += 1
        else:
            break
    # Check right 
    for i in range(r_q+1, n+1):
        if (str([i,c_q]) not in set_of_obstacles):
            counter += 1
        else:
            break
    # Check left 
    for i in range(r_q-1, 0, -1):
        if (str([i,c_q]) not in set_of_obstacles):
            counter += 1
        else:
            break
    # Upper right 
    x,y = r_q + 1, c_q + 1
    while (x < n+1 and y < n+1):
        if (str([x,y]) not in set_of_obstacles):
            counter += 1
            x += 1
            y += 1 
        else:
            break
    # Upper left 
    x,y = r_q - 1, c_q + 1
    while (x > 0 and y < n+1):
        if (str([x,y]) not in set_of_obstacles):
            counter += 1
            x -= 1
            y += 1  
        else:
            break
    # Bottom left 
    x,y = r_q - 1, c_q - 1
    while (x > 0 and y > 0):
        if (str([x,y]) not in set_of_obstacles):
            counter += 1
            x -= 1
            y -= 1  
        else:
            break
    # Bottom right 
    x,y = r_q + 1, c_q - 1
    while (x < n+1 and y > 0):
        if (str([x,y]) not in set_of_obstacles):
            counter += 1
            x += 1
            y -= 1  
        else:
            break
    return counter

if __name__ == '__main__':
    print(queensAttack(4, 0, 4, 4, []))
    # print(str([1,2]))
