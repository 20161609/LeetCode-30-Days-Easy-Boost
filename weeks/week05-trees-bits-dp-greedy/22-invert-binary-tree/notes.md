# Notes

## Link
https://leetcode.com/problems/invert-binary-tree/

# Code
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([TreeNode(left=root)])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
```

## Idea
- Use **BFS** with a queue to invert the binary tree level by level.  
- For each node, swap its left and right children.  
- Add existing children to the queue and continue until all nodes are processed.  
- Finally, return the original root (now inverted).

**Topic:** BFS / DFS (Tree)

## Complexity
- **Time:** O(n) — each node is visited once.  
- **Space:** O(n) — queue holds up to all nodes on the widest level.

## Gotcha
- Check for `None` before enqueueing children.  
- Works the same with DFS (stack) if desired.  
- Swapping must be done before enqueuing to ensure correct traversal.
