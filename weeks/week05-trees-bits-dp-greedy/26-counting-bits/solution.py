"""
Problem: Counting Bits
Link: https://leetcode.com/problems/counting-bits/
Topic: DP / Bits
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
from collections import deque, defaultdict

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n+1)        
        def backtrack(i, v, cnt):
            if v > n or 2**(i-1) > n:
                return
            answer[v] = cnt
            backtrack(i+1, v + 2**i, cnt+1), backtrack(i+1, v, cnt)
        backtrack(0, 0, 0)
        return answer