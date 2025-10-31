"""
Problem: Power of Two
Link: https://leetcode.com/problems/power-of-two/
Topic: Bit Manipulation
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i < n:
            i += 1
        return 2**i == n