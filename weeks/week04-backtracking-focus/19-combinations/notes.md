# Notes

## Link
https://leetcode.com/problems/combinations/

## Code
``` python
from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(i, box):
            if len(box) == k:
                answer.append(list(box))
                return
            needs, extra = k - len(box), n - i + 1
            if needs > extra: 
                return
            box.append(i), backtrack(i+1, box), box.pop(), backtrack(i+1, box)
        
        backtrack(1, deque())
        return answer
```

## Idea
- Generate all combinations of `k` numbers from `1` to `n` using **backtracking**.  
- At each step, decide whether to include the current number `i`.  
- If the current path’s length equals `k`, append a copy to `answer`.  
- Use pruning: if remaining numbers (`extra = n - i + 1`) are fewer than needed (`needs = k - len(box)`), stop exploring that branch.

**Topic:** Backtracking

## Complexity
- **Time:** O(C(n, k)) — each valid combination generated once.  
- **Space:** O(k) — recursion depth and temporary stack.

## Gotcha
- Always append with `list(box)` to avoid shared references.  
- Pruning (`needs > extra`) saves unnecessary recursion calls.  
- Start recursion from `1` to `n` inclusive.
