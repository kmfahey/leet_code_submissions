#!/usr/bin/python3

# Mini-Max Sum
#
# Given five positive integers, find the minimum and maximum values that can
# be calculated by summing exactly four of the five integers. Then print the
# respective minimum and maximum values as a single line of two space-separated
# long integers.
#
# Example
#
# arr = [1,3,5,7,9]
#
# The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24. The
# function prints
#
# 16 24
#
# Function Description
#
# Complete the miniMaxSum function in the editor below.
#
# miniMaxSum has the following parameter(s):
#
# arr: an array of 5 integers
#
# Print
#
# Print two space-separated integers on one line: the minimum sum and the
# maximum sum of 4 of 5 elements.

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maxSoFar = float("-inf")
    minSoFar = float("inf")
    for index in range(len(arr)):
        subArr = arr[:index] + arr[index+1:]
        subArrSum = sum(subArr)
        maxSoFar = max(maxSoFar, subArrSum)
        minSoFar = min(minSoFar, subArrSum)
    print(int(minSoFar), int(maxSoFar))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

