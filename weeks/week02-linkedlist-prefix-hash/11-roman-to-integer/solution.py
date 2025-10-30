"""
Problem: Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/
Topic: String Parsing
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, '-': 0}
        answer, prev = 0, '-'
        for i in range(n-1):
            if rom[s[i]] >= rom[s[i+1]]:
                answer += rom[s[i]] - rom[prev]
                prev = '-'
            else:
                prev = s[i]
        answer += rom[s[-1]] - rom[prev]

        return answer
