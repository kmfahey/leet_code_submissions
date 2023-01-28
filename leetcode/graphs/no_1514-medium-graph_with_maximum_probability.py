#!/usr/bin/python3

from typing import List
from heapq import heappop, heappush

# 1514. Path with Maximum Probability
# [Medium]
#
# You are given an undirected weighted graph of n nodes (0-indexed), represented
# by an edge list where edges[i] = [a, b] is an undirected edge connecting
# the nodes a and b with a probability of success of traversing that edge
# succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of
# success to go from start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted
# if it differs from the correct answer by at most 1e-5.

# Adapted from:
# https://leetcode.com/problems/path-with-maximum-probability/solutions/731655/python3-dijkstra-s-algo/

# Visible at:
# https://leetcode.com/problems/path-with-maximum-probability/submissions/886978330/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Interpret the edge list and probability list into a dict `graphNodes`
        # associating each node # with the node #s it has edges to, and a dict
        # `graphProbs` associating an edge (represented by a tuple of start node # to
        # end node #) with its probability.
        graphNodes, graphProbs = dict(), dict() #graphNodes with graphProbs
        for i, (u, v) in enumerate(edges):
            graphNodes.setdefault(u, []).append(v)
            graphNodes.setdefault(v, []).append(u)
            graphProbs[u, v] = graphProbs[v, u] = succProb[i]

        # A variation Dijkstra's algorithm, adjusted to the find the *max*
        # value rather than the *min*. Stores the probabilities on the heap in
        # negative, bc the heap maintained by heapq keeps the smallest elem on
        # top.
        #
        # Uses a heap of 2-tuples, where 2nd elem is the node number, and the
        # 1st elem is the probability of reaching that node, as a negative.
        # (Uses negatives bc the heap maintained by heapq puts the smallest elem
        # on top.) Starts with just the starting node on the heap, with prob -1
        # (an out-of-band initializing value to make future math on heap elem
        # 2-tuples 1st elem work).
        #
        # Loops over the heap while it's nonempty and the end node hasn't been
        # found. In each lopp, pops a node out of the heap. If the node has been
        # visited before, skips it. If the node is the end node, returns the
        # probability of reaching it.
        #
        # Otherwise, iterates across all edges linking it to other nodes. For
        # each linked node, pushes a 2-tuple onto the heap where the 2nd elem is
        # the node num and the 1st elem is the probability of reaching that elem
        # from start.
        #
        # If the heap is exhausted, returns 0.
        heap = [(-1, start)]
        seen = set()
        while heap:
            probability, nodeNum = heappop(heap)
            if nodeNum == end:
                return -probability
            seen.add(nodeNum)
            for seenNodeNum in graphNodes.get(nodeNum, []):
                if seenNodeNum in seen:
                    continue
                edgeProb = graphProbs.get((nodeNum, seenNodeNum), 0)
                combinedProb = probability * edgeProb
                heappush(heap, (combinedProb, seenNodeNum))
        return 0

solver = Solution()

print(solver.maxProbability(n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.2], start=0, end=2))


