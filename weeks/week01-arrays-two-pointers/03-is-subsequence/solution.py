"""
Problem: Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Topic: Two Pointers/Greedy
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        for c in t:
            if s_idx == len(s):
                return True
            if s[s_idx] == c:
                s_idx += 1
        
        return s_idx == len(s)