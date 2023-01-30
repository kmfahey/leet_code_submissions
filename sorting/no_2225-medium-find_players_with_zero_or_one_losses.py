#!/usr/bin/python3

from typing import List
from operator import itemgetter

# 2225. Find Players With Zero or One Losses
# Medium
# 
# You are given an integer array matches where matches[i] = [winneri, loseri]
# indicates that the player winneri defeated player loseri in a match.
# 
# Return a list answer of size 2 where:
# 
#     answer[0] is a list of all players that have not lost any matches.
#     answer[1] is a list of all players that have lost exactly one match.
# 
# The values in the two lists should be returned in increasing order.
# 
# Note:
# 
#     You should only consider the players that have played at least one match.
#     The testcases will be generated such that no two matches will have the same
#     outcome.

# Visible at:
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/submissions/888193761/

class Solution:
    # Straightforward in python. First I create a dict `lossCount` associating
    # every winner_i and loser_i to int 0. Then I iterate across the matches
    # list, taking `loser` and incrementing `lossCount[loser]`.
    #
    # Then I build a list of all keys in `lossCount` where value > 1, and use it
    # to delete all those keys from `lossCount`. I make a list `lossesToPlayers`
    # which is just (value, key) for every item in `lossCount`. I sort
    # that list, then divide it into two sublists, `noLossPlayers` and
    # `oneLossPlayers`, and return a pair of the two lists.
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossCount = {winner:0 for winner, _ in matches}
        # It's possible to have a player who appears in the record only in a
        # single loss, still need to the display them.
        lossCount.update({loser:0 for _, loser in matches})
        for winner, loser in matches:
            lossCount[loser] += 1
        lostMoreThanOnce = [player for player, lossCount in lossCount.items() if lossCount > 1]
        for player in lostMoreThanOnce:
            del lossCount[player]
        lossesToPlayers = [(lossCount, player) for player, lossCount in lossCount.items()]
        lossesToPlayers.sort()
        noLossPlayers = [player for lossCount, player in lossesToPlayers if lossCount == 0]
        oneLossPlayers = [player for lossCount, player in lossesToPlayers if lossCount == 1]
        return [noLossPlayers, oneLossPlayers]
