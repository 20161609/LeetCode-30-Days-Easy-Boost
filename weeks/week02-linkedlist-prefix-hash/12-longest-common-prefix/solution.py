"""
Problem: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Topic: String
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        box = []
        for i in range(min(len(s) for s in strs)):
            for s in strs:
                if strs[0][i] != s[i]:
                    return ''.join(box)
            box.append(strs[0][i])
        return ''.join(box)