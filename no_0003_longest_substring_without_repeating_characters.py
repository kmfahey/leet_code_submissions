#!/usr/bin/python3

# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without repeating
# characters.

# Not my solution; adapted from
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/811812/python-3-sliding-window-technique/ 
# My solution ran in O(n^m) time and was thwarted by a deliberately overlong
# testcase.

# Visible at
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/885253125/

class Solution:
    # This solution successively declares a starting index for the substr
    # being worked on `startIndex`. And then advances the end index for the
    # substr `endIndex`. A dict of chars already seen and the most recent index
    # each character was seen at, `charsAt`, is maintained.
    # 
    # With each new end index, that dict is checked to see if it already has
    # that character with an index that's greater than the current startIndex.
    # 
    # If so then the character already exists in the current substr, which
    # means it now contains a duplicate character and is no longer a candidate,
    # so a new value for `startIndex` is picked as the next index beyond the
    # duplicated character.

    def lengthOfLongestSubstring(self, strval: str) -> int:
        longestLenSoFar = 0
        startIndex = 0
        charsAt = dict()

        for endIndex in range(len(strval)):
            char = strval[endIndex]
            if char in charsAt and startIndex < charsAt[char] + 1:
                startIndex = charsAt[char] + 1
            charsAt[char] = endIndex
            thisSubstrLen = endIndex - startIndex + 1
            if thisSubstrLen > longestLenSoFar:
                longestLenSoFar = thisSubstrLen
        return longestLenSoFar

solver = Solution()

assert solver.lengthOfLongestSubstring("abcabcbb") == 3
assert solver.lengthOfLongestSubstring("bbbbb") == 1
assert solver.lengthOfLongestSubstring("pwwkew") == 3

