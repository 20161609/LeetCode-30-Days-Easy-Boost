# Notes

## Link
https://leetcode.com/problems/letter-case-permutation/

## Code
``` python
from collections import deque

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        answer = []
        def backtrack(i, box):
            if i == n:
                answer.append(''.join(box))
                return
            
            box.append(s[i])
            backtrack(i+1, box)
            box.pop()

            if s[i].isupper():
                box.append(s[i].lower())
                backtrack(i+1, box)
                box.pop()
            elif s[i].islower():
                box.append(s[i].upper())
                backtrack(i+1, box)
                box.pop()

        backtrack(0, deque())
        return answer
```

## Idea
- Use **backtracking** to explore all possible letter case combinations of the given string.  
- At each position `i`, always include the current character as-is.  
- If it’s a letter, also include its opposite case (`upper` ↔ `lower`) and recurse.  
- Append completed strings to `answer` when `i == n`.

**Topic:** Backtracking

## Complexity
- **Time:** O(2^n) — each letter can branch into two cases.  
- **Space:** O(n) — recursion depth and temporary list.

## Gotcha
- Digits remain unchanged (no branching).  
- Append and pop carefully to maintain the current path.  
- Use `deque` for efficient append/pop operations.
