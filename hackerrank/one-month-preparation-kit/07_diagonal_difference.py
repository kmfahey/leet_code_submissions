#!/bin/python3

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# 
# For example, the square matrix arr is shown below:
# 
# 1 2 3
# 4 5 6
# 9 8 9
# 
# The left-to-right diagonal = 1 + 5 + 9 = 19. The right to left diagonal = 3 +
# 5 + 9 = 17. Their absolute difference is | 15 - 17 | = 2.
# 
# Function description
# 
# Complete the diagonalDifference function in the editor below.
# 
# diagonalDifference takes the following parameter:
# 
#     int arr[n][m]: an array of integers
# 
# Return
# 
#     int: the absolute diagonal difference

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftDiagSum = sum([arr[index][index] for index in range(len(arr))])
    rightDiagSum = sum([arr[index][-index-1] for index in range(len(arr))])
    return abs(leftDiagSum - rightDiagSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

