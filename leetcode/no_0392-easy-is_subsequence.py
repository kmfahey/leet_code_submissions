#!/usr/bin/python3

# 392. Is Subsequence
# [Easy]
# 
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).


class Solution:
    # Iterates across the 1st string (to be found as a substr of the 2nd
    # string). For each character, returns False if it can't be found in the
    # current 2nd string. Otherwise takes the index of its 1st appearance in the
    # 2nd string. Then takes a substring of the right string starting at index+1
    # through end of string, and sets the right string equal to that. If control
    # flow reaches the end of the method, returns True.
    def isSubsequence(self, leftStrval: str, rightStrval: str) -> bool:
        for index in range(len(leftStrval)):
            char = leftStrval[index]
            if char not in rightStrval:
                return False
            index = rightStrval.index(char)
            rightStrval = rightStrval[index+1:]
        return True

solver = Solution()

assert solver.isSubsequence('abc', 'afghbijklclmn') == True
assert solver.isSubsequence('abc', "ahbgdc") == True

