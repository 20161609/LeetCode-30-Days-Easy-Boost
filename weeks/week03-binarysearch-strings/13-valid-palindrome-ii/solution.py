"""
Problem: Valid Palindrome II
Link: https://leetcode.com/problems/valid-palindrome-ii/
Topic: Two Pointers
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
# Paste your final accepted solution below.
# Example scaffold:
# class Solution:
#     def solve(self, *args, **kwargs):
#         pass

from collections import deque
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        stack = deque([[0,n-1,True]])
        while stack:
            l,r,chance = stack.pop()
            if l >= r:
                return True
            if s[l] == s[r]:
                stack.append([l+1,r-1,chance])
            elif chance:
                stack.append([l+1,r,False]), stack.append([l,r-1,False])

        return False