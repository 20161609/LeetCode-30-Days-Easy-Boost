# Notes

## Link
https://leetcode.com/problems/diameter-of-binary-tree/

## Code
``` python
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
```

## Idea
- Use **DFS** to compute the depth of each subtree while tracking the maximum path length.  
- For each node, the path through it equals `left_depth + right_depth + 1`.  
- Update `self.answer` with the largest path length seen so far.  
- Return `max(left_depth, right_depth) + 1` to represent the node’s depth.  
- After traversal, `self.answer` holds the diameter in node count.

**Topic:** DFS (Tree)

## Complexity
- **Time:** O(n) — each node is visited once.  
- **Space:** O(n) — recursion stack for a skewed tree.

## Gotcha
- Return `0` for `None` nodes to handle leaf boundaries.  
- The diameter is counted in nodes (`left + right + 1`), not edges.  
- Final result can be converted to edge count if required by subtracting 1.
