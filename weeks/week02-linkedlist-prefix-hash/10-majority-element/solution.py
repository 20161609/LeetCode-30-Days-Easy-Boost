"""
Problem: Majority Element
Link: https://leetcode.com/problems/majority-element/
Topic: Boyer–Moore
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)        
        for v in nums:
            freq[v] += 1
            if freq[v] > n // 2:
                return v