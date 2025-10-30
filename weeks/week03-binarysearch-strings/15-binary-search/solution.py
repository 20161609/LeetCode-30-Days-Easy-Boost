"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/
Topic: Binary Search
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, m, r = 0, (n-1)//2,n-1
        while l < m < r:
            if nums[m] > target: r = m
            elif nums[m] < target: l = m
            else: return m
            m = (l+r)//2

        if nums[l] == target: return l
        elif nums[r] == target: return r
        else: return -1