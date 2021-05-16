#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    divisible_arr = []
    both = []
    b.sort()
    for x in range(1, b[0]+1):
        if(divisible(x, a)):
            divisible_arr.append(x)
    for element in divisible_arr:
        if (another_div(element, b)):
            both.append(element)
    return len(both)
            
def divisible(n, lst):
    return all(map(lambda y: n%y == 0, lst))

def another_div(n, lst):
    return all(map(lambda i: i%n == 0, lst))
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
