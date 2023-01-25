#!/usr/bin/python

# Visible at:
# https://leetcode.com/problems/remove-element/submissions/885316791/

class Solution:
    # An easy-level problem, not much to document. Maintains an `offset` value,
    # initialized at 0. Generates each index in the list. While the value at
    # that index in the list is the one to eliminate, offset is incremented.
    # If offset now equals or exceeds the length of the list, the loop breaks.
    # Otherwise, the value at the index + the offset is copied to the cell at
    # the index. The return value is the length of the list minus the offset.
    def removeElement(self, nums: list[int], val: int) -> int:
        offset = 0
        incidence = 0
        for index in range(len(nums)):
            while index+offset < len(nums) and nums[index+offset] == val:
                offset += 1
            if index+offset >= len(nums):
                continue
            nums[index] = nums[index+offset]
        return len(nums) - offset

solver = Solution()

seq = [3,2,2,3]
newlen = solver.removeElement(seq, 3)
print(seq[:newlen])

seq = [0,1,2,2,3,0,4,2]
newlen = solver.removeElement(seq, 2)
print(seq[:newlen])
