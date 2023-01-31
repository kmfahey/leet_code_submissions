#!/bin/python3

# There are two n-element arrays of integers, A and B. Permute them into some
# A′ and B′ such that the relation A′[i] + B′[i] >= k holds for all i
# where 0 <= i <= n.
#
# There will be q queries consisting of A, B, and k. For each query, return YES
# if some permutation A′, B′ satisfying the relation exists. Otherwise,
# return NO.
#
# satisfying the relation exists. Otherwise, return NO.
#
# Example
#
# A = [0,1]
#
# B = [0,2]
#
# k = 1
#
# A valid A′, B′ is A′ = [1,0] and B′ = [0,2]: 1+0 >= 1 and 0+2 >= 1.
# Return YES.
#
# Function Description
#
# Complete the twoArrays function in the editor below. It should return a
# string, either YES or NO.
#
# twoArrays has the following parameter(s):
# 
#     int k: an integer
#     int A[n]: an array of integers
#     int B[n]: an array of integers
# 
# Returns
# - string: either YES or NO 

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B)
    satisfiable = True
    while len(A):
        elem = A.pop(0)
        for index in range(len(B)):
            if elem + B[index] >= k:
                B.pop(index)
                satisfiable = True
                break
            satisfiable = False
        if not satisfiable:
            break
    return "YES" if satisfiable else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()

