"""
Problem: Letter Case Permutation
Link: https://leetcode.com/problems/letter-case-permutation/
Topic: Backtracking
Difficulty: Medium

Note: Replace this file with your accepted solution.
"""
from collections import deque

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        answer = []
        def backtrack(i, box):
            if i == n:
                answer.append(''.join(box))
                return
            
            box.append(s[i])
            backtrack(i+1, box)
            box.pop()

            if s[i].isupper():
                box.append(s[i].lower())
                backtrack(i+1, box)
                box.pop()
            elif s[i].islower():
                box.append(s[i].upper())
                backtrack(i+1, box)
                box.pop()

        backtrack(0, deque())
        return answer
