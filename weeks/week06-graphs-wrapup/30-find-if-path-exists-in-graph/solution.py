"""
Problem: Find if Path Exists in Graph
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Topic: Graph BFS/DFS
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
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
    