# Notes

## Link
https://leetcode.com/problems/counting-bits/

## Code
``` python
from collections import deque, defaultdict
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n+1)        
        def backtrack(i, v, cnt):
            if v > n or 2**(i-1) > n:
                return
            answer[v] = cnt
            backtrack(i+1, v + 2**i, cnt+1), backtrack(i+1, v, cnt)
        backtrack(0, 0, 0)
        return answer
```

## Idea
- Use **backtracking** to fill an array of bit counts for all numbers up to `n`.  
- Function `backtrack(i, v, cnt)` recursively explores values formed by adding powers of 2.  
- Each state represents the count of set bits (`cnt`) for value `v`.  
- When `v > n` or the next power exceeds `n`, stop recursion.  
- Store the bit count in `answer[v]` for each valid number.

**Topic:** DP / Bits

## Complexity
- **Time:** O(n) — every number up to `n` is processed once.  
- **Space:** O(n) — output array storing counts.

## Gotcha
- Recursion depth grows with bit length of `n`.  
- Ensure termination conditions prevent overflow (`v > n`).  
- `answer[0] = 0` correctly represents zero having no set bits.
