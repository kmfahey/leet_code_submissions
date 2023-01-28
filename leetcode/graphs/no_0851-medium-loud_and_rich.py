#!/usr/bin/python3

import collections
from types import List

# 851. Loud and Rich
# [Medium]
# 
# There is a group of n people labeled from 0 to n - 1 where each person has a
# different amount of money and a different level of quietness.
#
# You are given an array richer where richer[i] = [ai, bi] indicates that ai has
# more money than bi and an integer array quiet where quiet[i] is the quietness
# of the ith person. All the given data in richer are logically correct (i.e.,
# the data will not lead you to a situation where x is richer than y and y is
# richer than x at the same time).
#
# Return an integer array answer where answer[x] = y if y is the least quiet
# person (that is, the person y with the smallest value of quiet[y]) among all
# people who definitely have equal to or more money than the person x.

# Adapted from:
# https://leetcode.com/problems/loud-and-rich/solutions/2714041/python-pure-topological-sort/

# Visible at:
# https://leetcode.com/problems/loud-and-rich/submissions/887059036/

class Solution:
    # So what we have is a set of edges that assign valences to the two nodes
    # connected. The starting node is in one class and the ending node is in the
    # other. The entire graph is set up in tiers. The edges aren't weighted but
    # they divide the graph into tiers.
    #
    # Then the *nodes* have weights. Nodes have an ordering by quietness level,
    # such that the last node is quietest.
    #
    # The return array is expected to have a cell for every node. For each
    # node x, the class being examined is all people who have equal to or more
    # money than node x. So a sub-graph of all nodes in the same richness tier
    # as x and all nodes in richer tiers. And if those nodes were ordered by
    # quietness, one would be the loudest. Since the quiet array lists nodes in
    # order by 'quietness level', the lowest value in that array is the loudest
    # nodes.
    #
    # So for each cell in the return array, consider all members of the same
    # richness tier as that node and all members of richer tiers. Of all of
    # those, that cell should have the index of the tiers member with the lowest
    # value in the quietness list.
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_count = [0 for _ in range(len(quiet))]
        graph = defaultdict(list)

        # The return array is initialized such that each cell is equal to its
        # index. In that sense its initial semantics says that array[x] = x, so
        # x is supposed to be the loudest node of all nodes as rich or richer
        # than x.
        answer = [idx for idx in range(len(quiet))]

        ## create the graph so that we go from the richer to the poorer
        for rich, poor in richer:
            graph[rich].append(poor)
            richer_count[poor] += 1

        # So richer_count is such that for each node x, richer_count[x] is the
        # number of nodes that are richer than that one.

        ## we include the richest ones.
        queue = collections.deque([])
        for person, rich_count in enumerate(richer_count):
            if not rich_count:
                queue.append(person)

        # The queue now contains the richest tier of the graph. For each
        # starting node in the queue, iterate over all starting nodes with edges
        # pointing to it. That set will all be as rich as each other, and the
        # starting node is a member of the set that are richer than them.
        # 
        # For each starting node, take current best guess at a louder
        # as-rich-or-richer node than that one. For each ending node, take the
        # current best guess of a louder as-rich-or-richer node than that one.
        # Pick between the nodes based on which has a lower value in the quiet
        # array; set the answer[endingNode] cell to that value. Decrement the
        # richer_count value for that ending node, and if it's become 0, add it
        # to the queue.

        while queue:
            person = queue.popleft()
            # pointer to the quietest person
            louder_person = answer[person]

            for poorer in graph[person]:
                # Pointer to the loudest-known node richer than than this node.
                louder_richer = answer[poorer]
                # On the answer list we are storing the pointer to the loudest
                # one. So for the next poorer we are going to store the pointer
                # which contains the loudest.
                answer[poorer] = min(louder_person, louder_richer, key = lambda prsn : quiet[prsn])
                richer_count[poorer] -= 1
                if not richer_count[poorer]:
                    queue.append(poorer)

        # At this point every node in the graph has been iterated over in order
        # from richest to poorest, and for each such node every node it points
        # to has been iterated over. So the cell in answer at index node will
        # have been visited in iteration for every node richer than it is, and
        # if that node is louder the cell will have been set to the louder node,
        # resulting in an array where each cell lists the loudest node among all
        # nodes as rich or richer.

        return answer
