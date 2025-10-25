"""
Problem: Two Sum II: Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Topic: Two Pointers
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: # number[l] + number[r] > target:
                r -= 1