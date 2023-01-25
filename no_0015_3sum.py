#!/usr/bin/python3

class Solution:
    # This solution first sorts the list. Then it advances 3 indexes through
    # the list: the first `index`, starts at 0 and counts as far as 2 short of
    # the end of the list. A set of all numbers found by at `index` is kept;
    # if the latest `index` finds a duplicate number, it's skipped. For each
    # `index`, the 2nd index, `left`, starts at `index`+1 and increases. The
    # 3rd, `right`, starts at length-1 and decreases. This continues until they
    # meet.
    #
    # A triplet is made out of the numbers at `index`, `left` and `right`. If
    # it sums to zero, it's added to the results; `left` is increased until the
    # number at `left` no longer equals the 2nd term in the triplet; and `right`
    # is decreased until the number at `right` no longer equals the 3rd term in
    # the triplet.
    #
    # Otherwise, if the sum was greater than 0, `right` is decreased. If the sum
    # was less than 0, `left` is increased. When the loop ends the results are
    # returned.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = list()
        nums.sort()
        firstNums = set()
        for index in range(len(nums)-2):
            if nums[index] in firstNums:
                continue
            firstNums.add(nums[index])
            left = index+1
            right = len(nums)-1
            while left < right:
                triplet = [nums[index], nums[left], nums[right]]
                if sum(triplet) == 0:
                    triplets.append(triplet)
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                    while left < right and nums[right] == triplet[2]:
                        right -= 1
                elif sum(triplet) > 0:
                    right -= 1
                else:
                    left += 1
        return triplets


solver = Solution()

print(solver.threeSum([-1,0,1,2,-1,-4]))
print(solver.threeSum([0,1,1]))
print(solver.threeSum([0,0,0]))

print(solver.threeSum([-10,5,-11,-15,7,-7,-10,-8,-3,13,9,-14,4,3,5,-7,13,1,-4,-11,5,9,-11,-4,14,0,3,-10,-3,-7,10,-5,13,14,-5,6,14,0,5,-12,-10,-1,-11,9,9,1,-13,0,-13,-1,4,0,-7,8,3,14,-15,-9,-10,-3,0,-15,-1,-2,6,9,11,6,-14,1,1,-9,-14,6,7,10,14,2,-13,-13,8,6,-6,8,-9,12,7,-9,-11,4,-4,-4,4,10,1,-12,-3,-2,1,-10,6,-13,-3,-1,0,11,-5,0,-2,-11,-6,-9,11,3,14,-13,0,7,-14,-4,-4,-11,-1,8,6,8,3]))
