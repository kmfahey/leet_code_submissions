#!/usr/bin/python3

# 205. Isomorphic Strings
# [Easy]
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

# Visible here:
# https://leetcode.com/problems/isomorphic-strings/submissions/885809791/

class Solution:
    def isIsomorphic(self, leftStrval: str, rightStrval: str) -> bool:
        def strvalToCharNums(strval):
            chars = [char for char in strval]
            charCount = 0
            for index in range(len(chars)):
                elem = chars[index]
                if isinstance(elem, str):
                    chars = [charCount if char == elem else char for char in chars]
                    charCount += 1
            return chars
        leftCharNums = strvalToCharNums(leftStrval)
        rightCharNums = strvalToCharNums(rightStrval)
        return leftCharNums == rightCharNums

