#!/bin/python3

import math
import os
import random
import re
import sys
import copy
import itertools


# Complete the absolutePermutation function below.


# def absolutePermutation(n, k):
#     possible_perms = []
#     master_array = [i for i in range(1, n+1)]
#     target = len(master_array)
#     skipped_list = {}
#     recursive_solution(0, [], master_array, k,
#                        possible_perms, skipped_list, target)
#     if possible_perms:
#         possible_perms.sort()
#         return(possible_perms[0])
#     else:
#         return([-1])

# def absolutePermutation(n, k):
#     master_array = [i for i in range(1, n+1)]
#     list_one = []
#     list_two = []
#     for i in range(n):
#         list_one.append(master_array[(i+k) % n])
#         list_two.append(master_array[(i-k) % n])
#     print(list_one)
#     print(list_two)
#     both_lists = [list_one, list_two]
#     both_lists.sort()
#     found = True
#     for i in range(len(both_lists[0])):
#         if abs(both_lists[0][i] - (i+1)) != k:
#             found = False
#             break
#     if found:
#         return both_lists[0]
#     else:
#         for i in range(len(both_lists[1])):
#             if abs(both_lists[1][i] - (i+1)) != k:
#                 found = False
#                 break
#     if(found):
#         return both_lists[1]
#     else:
#         return [-1]

def absolutePermutation(n, k):
    master_array = [i for i in range(1, n+1)]
    possible_placements = {}
    for number in master_array:
        first = number + k
        second = number - k
        # normal_index = (number + k) % n
        # opposite_index = (number - k) % n
        # if normal_index == opposite_index:
        #     if normal_index not in possible_placements:
        #         possible_placements[normal_index] = [number]
        #     else:
        #         possible_placements[normal_index].append(number)
        # else:
        #     if normal_index not in possible_placements:
        #         possible_placements[normal_index] = [number]
        #     else:
        #         possible_placements[normal_index].append(number)
        #     if opposite_index not in possible_placements:
        #         possible_placements[opposite_index] = [number]
        #     else:
        #         possible_placements[opposite_index].append(number)
    placements_array = []
    for index in range(len(master_array)):
        if index not in possible_placements:
            print("here")
            return([-1])
        placements_array.append(possible_placements[index])

    shuffeled_placements = [placements_array[(i+1) % n] for i in range(n)]

    all_possibilities = [
        possibility for possibility in itertools.product(*shuffeled_placements)]

    filtered_possibilities = [possibility for possibility in all_possibilities if len(
        possibility) == len(set(possibility))]

    if filtered_possibilities:
        filtered_possibilities.sort()
        return filtered_possibilities[0]
    else:
        return[-1]


def recursive_solution(posiition_to_fill, current_perm, remaining_values, k, possible_perms, skipped_list, target):
    if posiition_to_fill == target:
        possible_perms.append(current_perm)
        return
    for candidate in remaining_values:
        if (abs(candidate-(posiition_to_fill+1)) == k):
            # First check if we've decided to skip this placement
            if (posiition_to_fill in skipped_list):
                if(candidate in skipped_list[posiition_to_fill]):
                    continue
            # It may be in the solution at this spot
            # First we make deep copys of our lists to suit recursion
            copy_current_perm = copy.deepcopy(current_perm)
            copy_remaining_values = copy.deepcopy(remaining_values)
            # Then we append the item the the current permutation
            copy_current_perm.append(candidate)
            # And remove the item from the remaining values
            copy_remaining_values.remove(candidate)
            # Now we call the recursive solution for the next position
            recursive_solution(posiition_to_fill+1, copy_current_perm,
                               copy_remaining_values, k, possible_perms, skipped_list, target)

            # Or it may not be in this spot
            # First we make a deep copy of skipped list to avoid recursion conflicts
            copy_skipped_list = copy.deepcopy(skipped_list)
            if posiition_to_fill not in copy_skipped_list:
                copy_skipped_list[posiition_to_fill] = [candidate]
            else:
                copy_skipped_list[posiition_to_fill].append(candidate)

            # Now we call the function with the same position number but
            # skipped current possibility
            recursive_solution(posiition_to_fill, current_perm,
                               remaining_values, k, possible_perms, copy_skipped_list, target)
    # If there is no match in the remaining array, end the function
    return


if __name__ == '__main__':
    # tup = [1, 2, 3, 4]
    # print(tup[-5])
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(result)
