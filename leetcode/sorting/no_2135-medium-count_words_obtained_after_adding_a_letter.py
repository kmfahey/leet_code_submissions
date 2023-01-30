#!/usr/bin/python3

from typing import List

# 2135. Count Words Obtained After Adding a Letter
# Medium
# 
# You are given two 0-indexed arrays of strings startWords and targetWords. Each
# string consists of lowercase English letters only.
#
# For each string in targetWords, check if it is possible to choose a string
# from startWords and perform a conversion operation on it to be equal to that
# from targetWords.
#
# The conversion operation is described in the following two steps:
# 
#     Append any lowercase letter that is not present in the string to its end.
#         For example, if the string is "abc", the letters 'd', 'e', or 'y' can
#         be added to it, but not 'a'. If 'd' is added, the resulting string
#         will be "abcd".
#     Rearrange the letters of the new string in any arbitrary order.
#         For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and
#         so on. Note that it can also be rearranged to "abcd" itself.
# 
# Return the number of strings in targetWords that can be obtained by performing
# the operations on any string of startWords.
#
# Note that you will only be verifying if the string in targetWords can be
# obtained from a string in startWords by performing the operations. The strings
# in startWords do not actually change during this process.


# Adapted from:
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/solutions/2038966/python3-three-variations-brute-force-hashset-and-sorting-bitmask/

# Visible at:
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/submissions/888381967/

class Solution:
    # Every startWord has its letters sorted and joined into a new string, and
    # that string is added to a set. Every targetWord has its letters sorted,
    # but it's left as a list and add to a list.
    #
    # Then for each target word's sorted letters list, every possible sublist
    # missing one character is made, joined into a string, and that string is
    # checked for membership in the set of sorted startWord strings. If it's
    # found, anagramsFound is incremented and the inner loop is broken.
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordsSorted = set("".join(sorted(list(startWord))) for startWord in startWords)
        targetWordsSorted = [sorted(list(targetWord)) for targetWord in targetWords]
        anagramsFound = 0
        for target in targetWordsSorted:
            for index in range(len(target)):
                word = "".join(target[:index] + target[index+1:])
                if word in startWordsSorted:
                    anagramsFound += 1
                    break

        return anagramsFound

solver = Solution()

assert solver.wordCount(["ant","act","tack"], ["tack","act","acti"]) == 2

assert solver.wordCount(["ab","a"], ["abc","abcd"]) == 1

assert solver.wordCount(["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"], ["r","am","jg","umhjo","fov","lujy","b","uz","y"]) == 2


# Example 1:
# 
# Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
# Output: 2
# Explanation:
# - In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
# - There is no string in startWords that can be used to obtain targetWords[1] = "act".
#   Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
# - In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
# 
# Example 2:
# 
# Input: startWords = ["ab","a"], targetWords = ["abc","abcd"]
# Output: 1
# Explanation:
# - In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
# - There is no string in startWords that can be used to obtain targetWords[1] = "abcd".
# 
