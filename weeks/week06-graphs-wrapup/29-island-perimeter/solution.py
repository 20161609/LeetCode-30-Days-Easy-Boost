"""
Problem: Island Perimeter
Link: https://leetcode.com/problems/island-perimeter/
Topic: Grid / Counting
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
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