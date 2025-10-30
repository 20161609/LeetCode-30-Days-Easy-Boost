"""
Problem: Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
Topic: Prefix Sum
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cur, sum_nums = 0, sum(nums)
        for i in range(n):
            cur += nums[i]
            if cur - nums[i] ==  sum_nums - cur:
                # Left == Right
                return i

        return -1