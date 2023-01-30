#!/bin/python3

# You will be given a list of 32 bit unsigned integers. Flip all the bits (1 ->
# 0 and 0 -> 1) and return the result as an unsigned integer.
# 
# Example
# 
# n = (decimal) 9
# 
# (decimal) 9 == (binary) 1001 . We're working with 32 bits, so:
# 
# (binary) 00000000000000000000000000001001 == (decimal) 9
# 
# (binary) 11111111111111111111111111110110 == (decimal) 4294967286
# 
# Return (decimal) 4294967286
# 
# Function Description
# 
# Complete the flippingBits function in the editor below.
# 
# flippingBits has the following parameter(s):
# 
#     int n: an integer

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # For each place in [0,31], use 1 << place to build a binary number that's
    # got a 1 at that place and 0s otherwise, and OR n with that number. n's bit
    # at that place flips, all its other bits stay the same. Glad I found the
    # bitwise method, anything else feels cheap.
    for i in range(32):
        n = n ^ (1 << i)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

