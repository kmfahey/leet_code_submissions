#!/usr/bin/python3

# 724. Find Pivot Index
# 
# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to
# the left of the index is equal to the sum of all the numbers strictly to the
# index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because
# there are no elements to the left. This also applies to the right edge of the
# array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

# Visible here:
# https://leetcode.com/problems/find-pivot-index/submissions/885799413/

class Solution:
    # A simple solution. Iterates across the list, calculating the sum to the
    # left of the index, and the sum to the right. Returns the index if they're
    # equal. If the loop terminates without result, returns -1.
    def pivotIndex(self, nums: list[int]) -> int:
        for index in range(len(nums)):
            leftSum = 0 if index == 0 else sum(nums[:index])
            rightSum = 0 if index == len(nums) - 1 else sum(nums[index+1:])
            if leftSum == rightSum:
                return index
        return -1
