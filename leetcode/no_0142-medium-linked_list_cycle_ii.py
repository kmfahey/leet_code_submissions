#!/usr/bin/python3

# 142. Linked List Cycle II
# Medium
# 
# Given the head of a linked list, return the node where the cycle begins. If
# there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as
# a parameter.
#
# Do not modify the linked list.

# Visible here:
# https://leetcode.com/problems/linked-list-cycle-ii/submissions/886352066/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # When determining the presence of the loop, the fastNode reference travels twice
    # as fastNode as the slowNode reference.
    # Let x1 be the distance from list start to the start of the loop.
    # Let x2 be the distance from loop start to the point where slowNode and fastNode met.
    # Let x3 be the [forward] distance from the point where slowNode and fastNode met to
    # the start of the loop.
    # 
    # Fast travels twice as fastNode as slowNode.
    # 
    # Slow travelled f(s) = x1 + x2.
    # Fast travelled f(f) = x1 + x2 + x3 + x2.
    # 
    # Since fastNode travels twice as fastNode as slowNode,
    # f(f) = 2f(s)
    # x1 + x2 + x3 + x2 = 2(x1 + x2)
    # x1 + x2 + x3 + x2 = 2x1 + 2x2
    # x3 = x1
    # 
    # Which means if slowNode is reset to headNode, then fastNode and slowNode are repeatedly
    # advanced by 1 each, then when slowNode has travelled x1 it will be at loop
    # start, and fastNode has travelled x3 and will also be at loop start.
    #
    # So first zero-length and length-1 lists are detected. In either case None is
    # returned, a loop is impossible. Second the code searches for a loop using
    # the fast and slow pointer method. If no loop is found None is returned.
    #
    # Then since the [forward] distance from fastNode to loop start is equal
    # to the distance from headNode to loop start, slowNode is set equal to
    # headNode and both it and fastNode are advanced at 1/node per iteration
    # until they meet. When they both point to the same node, that node is the
    # start of the loop.
    def detectCycle(self, headNode):
        if headNode == None or headNode.next == None:
            return None

        slowNode = headNode.next
        fastNode = headNode.next.next

        while fastNode and fastNode.next:
            if slowNode == fastNode:
                break
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        if slowNode is not fastNode:
            return None

        # If loop exists. Start slowNode from
        # headNode and fastNode from meeting point.
        slowNode = headNode

        while (slowNode is not fastNode):
            slowNode = slowNode.next
            fastNode = fastNode.next

        return slowNode


solver = Solution()

head = ListNode(50)
head.next = ListNode(20)
head.next.next = ListNode(15)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(10)

head.next.next.next.next.next = head.next.next

assert solver.detectCycle(head).val == 15
