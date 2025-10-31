# Notes

## Link
https://leetcode.com/problems/find-if-path-exists-in-graph/

## Code
``` python
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b), graph[b].add(a)
        
        stack, visited = deque([source]), set([source])         
        while stack:
            node = stack.pop()            
            if node == destination:
                return True
            for nxt in graph[node]:
                if nxt in visited:
                    continue
                visited.add(nxt), stack.append(nxt)
        return False    
```

## Idea
- Build an **undirected graph** using an adjacency list from the given edges.  
- Use **DFS** (with a stack) or **BFS** to explore connected nodes starting from `source`.  
- Keep a `visited` set to prevent revisiting nodes.  
- If `destination` is reached, return `True`; otherwise, continue until the stack is empty.  
- If no path exists after traversal, return `False`.

**Topic:** Graph / DFS

## Complexity
- **Time:** O(V + E) — each vertex and edge is processed once.  
- **Space:** O(V + E) — adjacency list and visited set.

## Gotcha
- Make sure to iterate over `graph[node]`. 
- Mark nodes as visited **before** adding to the stack to avoid duplicates.  
- Works for both connected and disconnected graphs.
