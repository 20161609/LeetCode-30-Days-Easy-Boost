# Notes

## Link
https://leetcode.com/problems/binary-search/

## Code
``` python
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
```

## Idea
- Use two pointers `l` and `r` to define the current search range.  
- Compute the midpoint `m = (l + r) // 2` and compare `nums[m]` with `target`.  
- Narrow the range by moving `l` or `r` depending on whether `target` is smaller or larger.  
- Continue until the range collapses or `target` is found.  

## Complexity
- **Time:** O(log n)  
- **Space:** O(1)

## Gotcha
- Check both ends after the loop (`l` and `r`) to ensure the target isn’t missed.  
- Make sure to update `m` each iteration or risk infinite loops.
