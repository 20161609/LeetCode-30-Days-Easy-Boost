"""
Problem: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Topic: DFS (Tree)
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = deque([[TreeNode(left=root), 0]])

        #DFS
        while stack:
            node, depth = stack.pop()
            answer = max(answer, depth)

            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return answer