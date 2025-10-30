# Notes

## Link
https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Code
``` python
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
```

## Idea
- Use **DFS** with a stack to find the maximum depth of the binary tree.  
- Each stack element holds a node and its current depth.  
- Pop one node, update `answer` with the maximum depth, and push its children with `depth + 1`.  
- Continue until the stack is empty, then return the maximum depth found.

**Topic:** DFS (Tree)

## Complexity
- **Time:** O(n) — each node is visited once.  
- **Space:** O(n) — stack space in the worst case (skewed tree).

## Gotcha
- Return `0` if `root` is `None`.  
- Push children only if they exist.  
- Keep track of both node and depth in the stack.
