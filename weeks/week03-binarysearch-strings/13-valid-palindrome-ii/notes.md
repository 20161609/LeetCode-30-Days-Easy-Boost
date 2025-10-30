# Notes

## Link
https://leetcode.com/problems/valid-palindrome-ii/

## Code
``` python
# Paste your final accepted solution below.
# Example scaffold:
# class Solution:
#     def solve(self, *args, **kwargs):
#         pass

from collections import deque
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        stack = deque([[0,n-1,True]])
        while stack:
            l,r,chance = stack.pop()
            if l >= r:
                return True
            if s[l] == s[r]:
                stack.append([l+1,r-1,chance])
            elif chance:
                stack.append([l+1,r,False]), stack.append([l,r-1,False])

        return False
```

## Idea
- Use a stack (`deque`) to simulate checking with one allowed deletion.  
- Each state: `[l, r, chance]`.  
- If `s[l] == s[r]`, go inward.  
- If mismatch and `chance` left, try skipping either side.  
- If pointers cross, it's a valid palindrome.

## Complexity
- **Time:** O(n)  
- **Space:** O(n)

## Gotcha
- Stop when `l >= r`.  
- Handle both skip-left and skip-right cases.  
- Explicit stack avoids recursion.
