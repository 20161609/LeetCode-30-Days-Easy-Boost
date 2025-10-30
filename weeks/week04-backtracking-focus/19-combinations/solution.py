"""
Problem: Combinations
Link: https://leetcode.com/problems/combinations/
Topic: Backtracking
Difficulty: Medium

Note: Replace this file with your accepted solution.
"""
from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(i, box):
            if len(box) == k:
                answer.append(list(box))
                return
            needs, extra = k - len(box), n - i + 1
            if needs > extra: 
                return
            box.append(i), backtrack(i+1, box), box.pop(), backtrack(i+1, box)
        
        backtrack(1, deque())
        return answer