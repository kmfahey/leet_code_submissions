#!/bin/python3

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# 
# Note:
# - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# 
# Example
# 
# s = "12:01:00PM"
# 
# Return '12:01:00'.
# 
# s = "12:01:00AM"
# 
# Return '00:01:00'.
# 
# Function Description
# 
# Complete the timeConversion function in the editor below. It should return a
# new string representing the input time in 24 hour format.
# 
# timeConversion has the following parameter(s):
# 
#     string s: a time in 12 hour format
# 
# Returns
# 
#     string: the time in 24 hour format

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    matchObj = re.match(r"^(\d\d):(\d\d):(\d\d)([AP]M)$", s)
    hours, minutes, seconds, amOrPm = matchObj.groups()
    if hours == "12" and amOrPm == "AM":
        hours = "00"
    elif hours != "12" and amOrPm == "PM":
        hours = str(int(hours) + 12)
    return f"{hours}:{minutes}:{seconds}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

