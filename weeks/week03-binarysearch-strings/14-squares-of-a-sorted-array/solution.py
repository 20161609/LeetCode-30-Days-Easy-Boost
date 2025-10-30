"""
Problem: Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Topic: Two Pointers
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x**2 for x in nums)
