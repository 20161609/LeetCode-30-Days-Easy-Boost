"""
Problem: Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Topic: Hash / Sliding Window
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        box = defaultdict(int)        
        for i, v in enumerate(nums):
            if (v in box) and (i - box[v] <= k):
                return True
            box[v] = i
        return False