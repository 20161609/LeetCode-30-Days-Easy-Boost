"""
Problem: Symmetric Tree/
Link: https://leetcode.com/problems/symmetric-tree/
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs_flip(node):
            if node == None:
                return
            node.left, node.right = node.right, node.left
            dfs_flip(node.left), dfs_flip(node.right)

        dfs_flip(root.left)
        queue = deque([[root.left, root.right]])
        while queue:
            l, r = queue.popleft()
            if l==r==None:
                continue
            if ((l==None)^(r==None)) or (l.val != r.val):
                return False

            queue.append([l.left, r.left]), queue.append([l.right, r.right])
        
        return True