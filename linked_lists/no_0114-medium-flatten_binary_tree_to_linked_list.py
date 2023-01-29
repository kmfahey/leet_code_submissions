#!/usr/bin/python3

from typing import Optional

# 114. Flatten Binary Tree to Linked List
# Medium
# 
# Given the root of a binary tree, flatten the tree into a "linked list":
# 
# * The "linked list" should use the same TreeNode class where the right child
#   pointer points to the next node in the list and the left child pointer is
#   always null.

# * The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrderTraverse(node):
            if node is None:
                return None
            elif node.left is None:
                return node.right
            else:
                leftTraverse = preOrderTraverse(node.left)
                rightTraverse = preOrderTraverse(node.right)
                if leftTraverse is not None:
                    leftTraverse.right = rightTraverse
                    return leftTraverse
                else:
                    return rightTraverse
        root = preOrderTraverse(root)

unrollTree = lambda treeNode: [treeNode.val] + unrollTree(treeNode.right) if treeNode is not None else []

solver = Solution()

testTree = TreeNode(1, TreeNode(2, TreeNode(3),
                                   TreeNode(4)),
                       TreeNode(5, None,
                                   TreeNode(6)))

solver.flatten(testTree)

print(testTree.val)
