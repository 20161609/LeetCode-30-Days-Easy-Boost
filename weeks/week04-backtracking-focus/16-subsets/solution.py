"""
Problem: Subsets
Link: https://leetcode.com/problems/subsets/
Topic: Backtracking
Difficulty: Medium

Note: Replace this file with your accepted solution.
"""
from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer, stack = [], deque()
        def backtracking(i):
            if i == n:
                answer.append(list(stack))
                return
            backtracking(i+1)
            stack.append(nums[i])
            backtracking(i+1)
            stack.pop()

        backtracking(0)
        return answer
