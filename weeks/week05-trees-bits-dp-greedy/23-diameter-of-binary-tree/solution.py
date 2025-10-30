"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
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
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0        

        def dfs(node):
            if node == None:
                return 0
            left, right = dfs(node.left),dfs(node.right)
            self.answer = max(self.answer, left+right+1)            
            return max(left, right) + 1

        dfs(root)
        return self.answer