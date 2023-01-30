#!/usr/bin/python3

# Given an array of integers, calculate the ratios of its elements that are
# positive, negative, and zero. Print the decimal value of each fraction on a
# new line with 6 places after the decimal.
# 
# Note: This challenge introduces precision problems. The test cases are scaled
# to six decimal places, though answers with absolute error of up to 10^-4 are
# acceptable.
# 
# Example
# 
# arr = [1,1,0,-1,-1]
# There are elements, two positive, two negative and one zero. Their ratios are
# 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. Results are printed as:
# 
# 0.400000
# 0.400000
# 0.200000

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negCount = len(list(filter(lambda elem: elem < 0, arr)))
    posCount = len(list(filter(lambda elem: elem > 0, arr)))
    zeroCount = len(arr) - negCount - posCount
    negRatio = negCount / len(arr)
    posRatio = posCount / len(arr)
    zeroRatio = zeroCount / len(arr)
    print(f"{posRatio:.6f}\n{negRatio:.6f}\n{zeroRatio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

