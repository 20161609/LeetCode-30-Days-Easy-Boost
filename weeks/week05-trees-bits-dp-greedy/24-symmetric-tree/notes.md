# Notes

## Link
https://leetcode.com/problems/symmetric-tree/

``` python
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
```

## Idea
- First, **mirror** the left subtree using a helper function `dfs_flip`.  
- Then, use **BFS** to compare the mirrored left subtree with the original right subtree.  
- For each node pair `(l, r)`:
  - Skip if both are `None`.  
  - If one is `None` or values differ, return `False`.  
  - Otherwise, enqueue their children `(l.left, r.left)` and `(l.right, r.right)`.  
- If all levels match, the tree is symmetric.

**Topic:** DFS (Tree)

## Complexity
- **Time:** O(n) — every node is visited once during mirroring and comparison.  
- **Space:** O(n) — queue space for BFS traversal.

## Gotcha
- Be careful not to mix up the mirrored left subtree and the original right one.  
- Flipping must happen before comparison begins.  
- Handle `None` checks explicitly to avoid attribute errors.
