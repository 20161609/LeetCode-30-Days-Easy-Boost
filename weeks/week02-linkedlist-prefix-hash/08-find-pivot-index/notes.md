# Notes

## Link
https://leetcode.com/problems/find-pivot-index/

## Code
``` python
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
```

## Idea
- Use prefix sums to find the **pivot index** where the sum of all elements to the left equals the sum of all elements to the right.  
- Maintain a running cumulative sum `cur` as you iterate.  
- For each index `i`, the left sum is `cur - nums[i]`, and the right sum is `sum_nums - cur`.  
- If they are equal, return the current index as the pivot.  
- If no such index exists, return `-1`.

**Topic:** Prefix Sum

## Complexity
- **Time:** O(n) — single traversal of the array.  
- **Space:** O(1) — uses only a few variables.

## Gotcha
- Make sure to update `cur` *after* adding `nums[i]` before comparison.  
- The pivot can appear at index `0` or at the end — handle edge cases correctly.  
- Avoid using extra prefix-sum arrays; this solution already works in constant space.
