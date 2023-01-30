#!/usr/bin/python3

from typing import List

# 435. Non-overlapping Intervals
# Medium
# 
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.

# Adapted from:
# https://leetcode.com/problems/non-overlapping-intervals/solutions/3108249/best-solution-explained-with-illustrations/

# Visible at:
# https://leetcode.com/problems/non-overlapping-intervals/submissions/888361058/

class Solution:
    # This solution removes the minimum number of intervals. I don't understand
    # why and out of 5 pages of solutions on leetcode plus several found on
    # google, nobody thinks to explain how their solution can be relied upon to
    # remove the minimum number. I know it's not a guarantee because my first
    # solution didn't. Anyway, here's an answer I don't understand because
    # nobody bothered to explain themselves.
    #
    # Anyway this solution keeps a value for the endpoint of the last pair
    # examined, `lastEnd`, initialized at -Infinity. The intervals list is
    # sorted by endpoint ascending. Then the list is iterated through. For
    # each pair, if its starting point is less than the stored endpoint of the
    # last pair, the counter is incremented. Otherwise `lastEnd` is updated to
    # be equal to the endpoint of the current pair. At the end the counter is
    # returned.
    #
    # I consider this answer incomplete. Have asked questions about this problem
    # in a few places. Will update this when I finally get an answer how the
    # minimum-number requirement is met.
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        lastEnd = float("-inf")
        intervals.sort(key=lambda pair: pair[1])
        for pair in intervals:
            pairStart, pairEnd = pair
            if pairStart >= lastEnd:
                lastEnd = pairEnd
            else:
                counter += 1
        return counter

solver = Solution()

assert solver.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1

assert solver.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2

assert solver.eraseOverlapIntervals([[1,2],[2,3]]) == 0

