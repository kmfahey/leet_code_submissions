##!/usr/bin/python3

from typing import Optional

# 114. Flatten Binary Tree to Linked List
# Medium
# 
# Given the root of a binary tree, flatten the tree into a "linked list":
# 
# * The "linked list" should use the same TreeNode class where the right child
#   pointer points to the next node in the list and the left child pointer is
#   always null.
#
# * The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#
# Definition for a binary tree node.
# 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Adapted from:
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/37227/python-easy-to-understand-recursive-solution-with-explaination/

# Visible at:
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/887689638/


class Solution:
    # This recursive solution loops while root is not None. If root.left is
    # not None, it's flattened, which means root.left.left is now None and
    # root.left.right is a flattened series of all nodes under root.left.
    #
    # Then the leftNode pointer is advanced to the last node in the
    # now-flattened leftNode sequence. The root's right node is saved as
    # rightNode, then root.right is set to root.left, root.left is set to None,
    # and the leftNode pointer's right node is set to rightNode. In this way the
    # original subtree under root.right is attached at the end of the flattened
    # left subtree, the flattened left subtree is set as the root's right node,
    # and the root's left node is nilled.
    #
    # Then, whether root.left was None or not, root is set to root.right. So the
    # while loop advances the root pointer down the right node side of the tree,
    # and if there's a root.left subtree it's flattened, the pre-existing right
    # subtree is attached to the right pointer of its terminal node, the left
    # subtree is attached to the root node's right pointer, and the root node's
    # left pointer is nilled.
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root is not None:
            if root.left is not None:
                self.flatten(root.left)
                leftNode = root.left
                while leftNode.right:
                    leftNode = leftNode.right
                rightNode = root.right
                root.right = root.left
                root.left = None
                leftNode.right = rightNode
            root = root.right
