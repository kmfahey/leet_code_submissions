#!/usr/bin/python3

import pprint

# 48. Rotate Image
# [Medium]
#
# You are given an n x n 2D matrix representing an image, rotate the image by 90
# degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.

# Visible at:
# https://leetcode.com/problems/rotate-image/submissions/885338570/

class Solution:
    # For a matrix, rotating 90 degrees clockwise is equivelant to vertically
    # reversing the matrix (bottom row becomes top, etc.) and then transposing
    # it (columns become rows, rows become columns).
    #
    # First, since the matrix is represented as a list whose cells represent
    # rows containing lists whose cells represent columns, vertically reversing
    # the list is as easy as swapping the topmost cell of the outer list with
    # the bottommost, then the 2nd-to-topmost with the 2nd-to-bottommost, and so
    # on.
    #
    # Second, transposing a matrix can be thought of as taking its mirror
    # image if the mirror ran diagonally from top-left to bottom-right. For
    # x ordinates between 0 and n - 1, for y ordinates between 0 and the x
    # ordinate, exchange the value at (x, y) for the value at (y, x).
    def rotate(self, matrix: list[list[int]]) -> None:
        if len(matrix) == 0 or len(matrix) == 1:
            return

        # reverse
        bottomIndex = 0
        topIndex = len(matrix) -1
        while bottomIndex < topIndex:
            matrix[bottomIndex], matrix[topIndex] = matrix[topIndex], matrix[bottomIndex]
            bottomIndex += 1
            topIndex -= 1

        # transpose 
        for xOrd in range(len(matrix)):
            for yOrd in range(xOrd):
                matrix[xOrd][yOrd], matrix[yOrd][xOrd] = matrix[yOrd][xOrd], matrix[xOrd][yOrd]

solver = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
pprint.pprint(matrix)
solver.rotate(matrix)
pprint.pprint(matrix)
