"""
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Topic: Kadane (DP-1D)
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = nums[0]
        answer = nums[0]
        for i in range(1, n):
            nums[i] += nums[i-1]
            answer = nums[i] if answer < nums[i] else answer
            answer = nums[i] - min_sum if answer < nums[i] - min_sum else answer
            min_sum = nums[i] if min_sum > nums[i] else min_sum

        return nums[-1] - min_sum