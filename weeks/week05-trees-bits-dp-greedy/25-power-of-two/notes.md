# Notes

## Link
https://leetcode.com/problems/power-of-two/

## Code
``` python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i < n: i += 1
        return 2**i == n
```

## Idea
- Repeatedly compare powers of 2 (`2**i`) with the target number `n`.  
- Increment `i` until `2**i` is no longer less than `n`.  
- Return `True` if an exact match is found; otherwise, `False`.

**Topic:** Bit Manipulation

## Complexity
- **Time:** O(log n) — increases `i` until `2**i` exceeds `n`.  
- **Space:** O(1)

## Gotcha
- Return `False` for all non-positive numbers (`n <= 0`).  
- Exponentiation grows quickly, so the loop runs in logarithmic time.
