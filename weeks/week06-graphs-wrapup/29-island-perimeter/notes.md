# Notes

## Link
https://leetcode.com/problems/island-perimeter/

## Code
``` python
from collections import defaultdict, deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        queue, visited = deque(), defaultdict(bool)
        answer = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0 or visited[(x,y)]:
                    continue
                queue.append((x,y))
                visited[(x,y)] = True
                while queue:
                    x, y = queue.popleft()
                    for nx, ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                        if not (0<=nx<w and 0<=ny<h) or grid[ny][nx] == 0:
                            answer += 1
                            continue
                        if visited[(nx,ny)]:
                            continue
                        visited[(nx,ny)] = True
                        queue.append((nx,ny))
        return answer
```

## Idea
- Traverse the grid using **BFS** to find connected land cells (`1`).  
- For each land cell, check its four directions:  
  - If it touches the boundary or water (`0`), add `1` to the perimeter.  
  - Otherwise, enqueue unvisited neighboring land cells.  
- Use a `visited` map to prevent reprocessing the same cell.  
- Sum up all outer edges to get the total island perimeter.

**Topic:** Grid / Counting

## Complexity
- **Time:** O(n^2) — visit each cell at most once.  
- **Space:** O(n^2) — for the visited map and BFS queue.

## Gotcha
- Must check bounds before accessing `grid[ny][nx]`.  
- Each water edge or border contributes `1` to the perimeter.  
- Works for a single island; no need to handle multiple disjoint islands in this problem.
