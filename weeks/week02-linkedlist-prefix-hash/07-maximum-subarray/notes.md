# Notes

## Code
``` python
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
```

## Link
https://leetcode.com/problems/maximum-subarray/

## Idea
- Use prefix sums to keep track of the running total of elements.  
- Maintain a variable `min_sum` for the smallest prefix sum seen so far.  
- For each position, compute the potential maximum subarray sum as `current_sum - min_sum`.  
- Update `answer` and `min_sum` at every step accordingly.  
- This is a variant of **Kadane’s Algorithm** implemented via prefix-sum tracking.

**Topic:** Kadane (DP-1D)

## Complexity
- **Time:** O(n) — single pass through the array.  
- **Space:** O(1) — uses only constant extra memory.

## Gotcha
- The algorithm **modifies `nums` in-place** (accumulating prefix sums).  
- Initialize correctly with `min_sum = nums[0]` and `answer = nums[0]`.  
- If the first number is negative, that initialization is still valid since the logic adjusts dynamically.
