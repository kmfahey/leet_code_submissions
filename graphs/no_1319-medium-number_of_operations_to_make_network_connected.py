#!/usr/bin/python3

from typing import List

# 1319. Number of Operations to Make Network Connected
# Medium
# 
# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [ai, bi] represents a
# connection between computers ai and bi. Any computer can reach any other
# computer directly or indirectly through the network.
#
# You are given an initial computer network connections. You can extract certain
# cables between two directly connected computers, and place them between any
# pair of disconnected computers to make them directly connected.
#
# Return the minimum number of times you need to do this in order to make all
# the computers connected. If it is not possible, return -1.

class Solution:
    # This problem actually calls for determining how many disconnected
    # subgraphs are in the input. However, to connect n nodes, one needs n - 1
    # edges. So if len(connections) < n - 1, return -1.
    # 
    # After that, build an adjacency list. Then, for each node in the graph,
    # check if it's been visited. If not, perform a depth-first traversal
    # starting at that node, marking that node and all nodes reachable from it
    # as visited. Then increment numberOfComponents. Once all nodes have been
    # visited, there are numberOfComponents disconnected sub-graphs. They'll
    # take numberOfComponents - 1 edges to connect, so that's the return value.
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def depthFirstTraversal(graph, startNode, visited):
            visited[startNode] = True
            for endNode in graph[startNode]:
                if visited[endNode]:
                    continue
                depthFirstTraversal(graph, endNode, visited)

        if len(connections) < n -1:
            return -1

        graph = [[] for _ in range(n)]

        for lhNode, rhNode in connections:
            graph[lhNode].append(rhNode)
            graph[rhNode].append(lhNode)

        numberOfComponents = 0

        visited = [False]*n

        for node in range(len(graph)):
            if visited[node]:
                continue
            depthFirstTraversal(graph, node, visited)
            numberOfComponents += 1

        return numberOfComponents - 1

solver = Solution()

print(solver.makeConnected(4, [[0,1],[0,2],[1,2]]))
print(solver.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(solver.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))


