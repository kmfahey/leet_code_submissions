#!/bin/python3

# Two players are playing a game of Tower Breakers! Player 1 always moves first,
# and both players always play optimally. The rules of the game are as follows:
# 
#     Initially there are n towers.
#     Each tower is of height m.
#     The players move in alternating turns.
#     In each turn, a player can choose a tower of height x and reduce its
#         height to y, where 1 <= y < x and y evenly divides into x.
#     If the current player is unable to make a move, they lose the game.
# 
# Given the values of n and m, determine which player will win. If the first
# player wins, return 1. Otherwise, return 2.
# 
# Example.
# 
# n = 2
# m = 6
# 
# There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
# - remove 3 pieces from a tower to leave 3 as 6 % 3 == 0.
# - remove 5 pieces to leave 1.
# 
# Let Player 1 remove 3. Now the towers are 3 and 6 units tall.
# 
# Player 2 matches the move. Now the towers are both 3 units tall.
# 
# Now Player 1 has only one move.
# 
# Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
# 
# Player 2 matches again. Towers are both 1 unit tall.
# 
# Player 1 has no move and loses. Return 2.
# 
# Function Description
# 
# Complete the towerBreakers function in the editor below.
# 
# towerBreakers has the following paramter(s):
# 
#     int n: the number of towers
#     int m: the height of each tower
# 
# Returns
# 
#     int: the winner of the game

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    moveCount = 0
    testM = m
    while testM > 1:
        for newHeight in range(1, testM):
            if testM % newHeight == 0:
                testM = newHeight
                moveCount += 1
                break
        if testM == 1:
            break
    totalMoves = moveCount * n
    return 2 if totalMoves % 2 == 0 else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

