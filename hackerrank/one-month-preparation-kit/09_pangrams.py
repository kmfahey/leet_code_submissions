#!/bin/python3

# A pangram is a string that contains every letter of the alphabet. Given a
# sentence determine whether it is a pangram in the English alphabet. Ignore
# case. Return either pangram or not pangram as appropriate.
#
# Example
#
# s = 'The quick brown fox jumps over the lazy dog'
#
# The string contains all letters in the English alphabet, so return pangram.
#
# Function Description
#
# Complete the function pangrams in the editor below. It should return the
# string pangram if the input string is a pangram. Otherwise, it should return
# not pangram.
#
# pangrams has the following parameter(s):
#
#     string s: a string to test
#
# Returns
#
#     string: either pangram or not pangram


import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = set("abcedfghijklmnopqrstuvwxyz")
    s = s.lower()
    s = ''.join(re.split("[^a-z]", s))
    return 'pangram' if set(s) == alphabet else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

