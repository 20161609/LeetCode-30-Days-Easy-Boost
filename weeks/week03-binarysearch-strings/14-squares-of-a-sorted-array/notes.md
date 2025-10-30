# Notes

## Link
https://leetcode.com/problems/squares-of-a-sorted-array/

## Code
``` python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x**2 for x in nums)
```

## Idea
- Square every element and sort the results.  
- Python’s `sorted()` handles sorting efficiently.

## Complexity
- **Time:** O(n log n)  
- **Space:** O(n)

## Gotcha
- Negative numbers become positive after squaring.  
- Sorting is required to restore non-decreasing order.
