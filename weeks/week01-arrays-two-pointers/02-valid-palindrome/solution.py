"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Topic: Two Pointers
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        box = []
        box = deque()
        for c in s:
            if c.isalpha() or c.isnumeric():
                box.append(c.lower())
        s = ''.join(box)
        return s==s[::-1]