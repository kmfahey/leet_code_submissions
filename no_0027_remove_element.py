#!/usr/bin/python

# 27. Remove Element
# 
# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
# 
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.
# 
# int k = removeElement(nums, val); // Calls your implementation
# 
# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 
# If all assertions pass, then your solution will be accepted.

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
