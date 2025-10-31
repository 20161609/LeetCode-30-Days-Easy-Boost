"""
Problem: Assign Cookies
Link: https://leetcode.com/problems/assign-cookies/
Topic: Greedy
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()        
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i+= 1
            j += 1

        return i