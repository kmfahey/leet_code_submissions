#!/usr/bin/python3

# 226. Invert Binary Tree
# [Easy]
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Visible here:
# https://leetcode.com/problems/invert-binary-tree/submissions/885396128/

class Solution:
    # A simple recursive algorithm solves this; implemented using a private
    # function. The recursive private function instances a new TreeNode with
    # the same val as its argument. For each child node of its argument, if
    # non-None, the function is called to copy that node with its return value
    # assigned to the opposite child of the new node.
    #
    # The function returns None if called with None, otherwise returns the
    # result of calling the private function with the root node that is its
    # argument.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invTreeCopy(node):
            newNode = TreeNode(node.val)
            if node.left is not None:
                newNode.right = invTreeCopy(node.left)
            if node.right is not None:
                newNode.left = invTreeCopy(node.right)
            return newNode
        if root is None:
            return None
        else:
            return invTreeCopy(root)



