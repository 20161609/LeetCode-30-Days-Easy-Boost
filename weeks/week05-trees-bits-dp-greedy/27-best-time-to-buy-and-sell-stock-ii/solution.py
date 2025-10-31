"""
Problem: Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Topic: Greedy
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, stack = 0, deque()
        for p in prices:
            if stack and stack[-1] > p:
                answer += stack[-1] - stack[0]
                stack.clear()
            stack.append(p)
        if stack:
            answer += stack[-1] - stack[0]
        return answer