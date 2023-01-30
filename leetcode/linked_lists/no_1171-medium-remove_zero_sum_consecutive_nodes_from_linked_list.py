# Definition for singly-linked list.

from typing import Optional

# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# [Medium}
# 
# Given the head of a linked list, we repeatedly delete consecutive sequences of
# nodes that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list. You may return any
# such answer.

# Adapted from pseudocode found on a site I've since lost track of in my browser
# history, sorry.

# Visible at:
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/submissions/887627149/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # This solution calculates the prefix sum at each node in the list and
    # stores it to a dict as the key with the node that had that sum as the
    # value. Logically if the same sum is computed a second time it will
    # overwrite the earlier value for that key in the mapping. In this way the
    # mapping only stores the *last* node to have that prefix sum.
    #
    # (It also creates a ahead-of-the-head-node-node called dummy, and sets head
    # to be its next.)
    #
    # Since with prefix sums if the same sum occurs at node_A and node_B, then
    # all nodes between node_A and node_B will have a cumulative sum of zero and
    # can be dropped.
    #
    # The list is looped through a second time, calculating prefix sums again.
    # This time the loop will find the *first* node with a given prefix sum,
    # while the mapping holds the *last* node with that sum. If a computed
    # sum is found in the mapping but the nodes are different, then there's a
    # sum-zero sublist that can be dropped; so the current node of the loop is
    # linked to the node found in the mapping with the same prefix sum. This
    # repeats until the list is exhausted a second time, then the dummy's next
    # node is returned.
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prefixSum = 0
        lastNode = dummyNode
        thisNode = dummyNode.next
        mapping = {0:dummyNode}
        nodesSum = 0
        while head is not None:
            nodesSum += head.val
            mapping[nodesSum] = head
            head = head.next
        head = dummyNode
        nodesSum = 0
        while head is not None:
            nodesSum += head.val
            tempNode = mapping[nodesSum]
            if tempNode is not head:
                head.next = tempNode.next
            head = head.next
        return dummyNode.next

solver = Solution()

testList = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))

unrollList = lambda node: [node.val] + unrollList(node.next) if node is not None else []

print(unrollList(solver.removeZeroSumSublists(testList)))
