# Notes

## Link
https://leetcode.com/problems/generate-parentheses/

## Code
``` python
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        box = deque()
        def backtrack(i, stack):
            if stack > n*2 - i + 1:
                return
            
            if i > n*2:
                answer.append(''.join(box))
                return

            if stack < n:
                box.append('('), backtrack(i+1, stack+1), box.pop()

            if stack:
                box.append(')'), backtrack(i+1, stack-1), box.pop()

        backtrack(1, 0)
        return answer
```

## Idea
- Use **backtracking** to build all valid parentheses sequences.  
- Track the number of opened parentheses (`stack`) and total positions `i`.  
- Add `'('` when `stack < n`, and add `')'` when `stack > 0`.  
- When `i` exceeds `2 * n`, append the completed string to `answer`.  
- Prune early if `stack > n * 2 - i + 1` (invalid state).

**Topic:** Backtracking

## Complexity
- **Time:** O(4ⁿ / √n) — number of valid parentheses combinations (Catalan number).  
- **Space:** O(n) — recursion depth and current path.

## Gotcha
- Ensure you don’t add `')'` before `'('` exists (keep `stack > 0`).  
- Prune invalid states early for efficiency.  
- Use `deque` for quick append/pop during recursion.
