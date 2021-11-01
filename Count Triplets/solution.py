import math
import os
import random
import re
import sys

def populate_dic(arr):
    output = {}
    for index in range(len(arr)):
        number = arr[index]
        if number in output:
            output[number].append(index)
        else:
            output[number] = [index]
    return output

def countTriplets(arr, r):
    master_dic = populate_dic(arr)
    total_count = 0
    if r == 1:
        for number in master_dic:
            if len(master_dic[number]) >= 3:
                total_count += math.comb(len(master_dic[number]), 3)
    else:
        for first_number in master_dic:
            second_number = first_number * r
            third_number = second_number * r

            if second_number in master_dic and third_number in master_dic:
                first_index_array = master_dic[first_number]
                second_index_array = master_dic[second_number]
                third_index_array = master_dic[third_number]

                second_mapping = {}

                third_pointer = 0
                for n in second_index_array:
                    if third_pointer > len(third_index_array) - 1:
                        second_mapping[n] = 0
                        continue
                    # Set third pointer
                    while third_index_array[third_pointer] < n:
                        third_pointer += 1
                        if third_pointer > len(third_index_array) - 1:
                            break
                    
                    if third_pointer > len(third_index_array) - 1:
                        second_mapping[n] = 0
                    else:
                        numbers_remaining = len(third_index_array) - third_pointer
                        second_mapping[n] = numbers_remaining

                second_total_mappings = {}

                current_total = 0
                how_many_from_second_row = 0

                second_total_mappings[how_many_from_second_row] = current_total

                current_index = len(second_index_array) - 1

                while current_index >= 0:
                    to_add = second_mapping[second_index_array[current_index]]
                    how_many_from_second_row += 1
                    current_total += to_add
                    second_total_mappings[how_many_from_second_row] = current_total                    
                    current_index -= 1
            
                second_pointer = 0

                for n in first_index_array:
                    if second_pointer > len(second_index_array) - 1:
                        break
                    # Set second pointer 
                    while second_index_array[second_pointer] < n:
                        second_pointer += 1
                        if second_pointer > len(second_index_array) - 1:
                            break
                    
                    if second_pointer <= len(second_index_array) - 1:
                        number_from_second_row = len(second_index_array) - second_pointer
                        total_count += second_total_mappings[number_from_second_row]
    return (total_count)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
