"""
Problem: Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/
Topic: Backtracking
Difficulty: Medium

Note: Replace this file with your accepted solution.
"""
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        box = deque()
        def backtrack(i, stack):
            if stack > n*2 - i + 1:
                return
            
            if i > n*2:
                answer.append(''.join(box))
                return

            if stack < n:
                box.append('('), backtrack(i+1, stack+1), box.pop()

            if stack:
                box.append(')'), backtrack(i+1, stack-1), box.pop()

        backtrack(1, 0)
        return answer