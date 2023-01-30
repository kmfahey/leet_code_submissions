#!/bin/python3

# Given an array of integers, where all elements but one occur twice, find the
# unique element.
#
# Example
#
# a = [1,2,3,4,3,2,1]
#
# The unique element is 4.
#
# Function Description
#
# Complete the lonelyinteger function in the editor below.
#
# lonelyinteger has the following parameter(s):
#
#     int a[n]: an array of integers
#
# Returns
#
#     int: the element that occurs only once

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    return [integer for integer in set(a) if a.count(integer) == 1][0]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

