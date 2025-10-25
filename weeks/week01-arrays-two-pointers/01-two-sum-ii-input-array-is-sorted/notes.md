# Notes

## Link
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Code
``` python
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
```

## Idea
- Use **two pointers** starting from both ends of the sorted array.  
- If the current sum is smaller than `target`, move the left pointer to increase the sum.  
- If the current sum is greater than `target`, move the right pointer to decrease the sum.  
- When the sum matches the target, return the 1-based indices `[l+1, r+1]`.  

**Topic:** Two Pointers

## Complexity
- Time: O(n) — each pointer moves at most once across the array  
- Space: O(1) — constant extra memory  

## Gotcha
- Remember the array is **1-indexed** in the output.  
- Make sure to handle duplicates properly — no need to skip them since we only need one valid pair.  
- Avoid integer overflow in languages without automatic big-integer handling (not an issue in Python).  