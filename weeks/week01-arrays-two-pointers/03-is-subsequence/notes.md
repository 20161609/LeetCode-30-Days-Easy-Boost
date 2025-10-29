# Notes

## Link
https://leetcode.com/problems/is-subsequence/

## Code
``` python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        for c in t:
            if s_idx == len(s):
                return True
            if s[s_idx] == c:
                s_idx += 1
        
        return s_idx == len(s)
```

## Idea
- Use **two pointers** — one for the smaller string `s`, one for the longer string `t`.  
- Iterate through `t`; whenever `t[i]` matches the current character of `s`, move the pointer in `s`.  
- If all characters in `s` are matched before `t` ends, return `True`.  
- This is effectively a **greedy** approach: always take the first possible matching character in order.

**Topic:** Two Pointers / Greedy

## Complexity
- **Time:** O(n) — where `n = len(t)`, since we scan `t` once.  
- **Space:** O(1) — only uses a few integer counters.

## Gotcha
- When `s` is empty (`""`), it’s always a subsequence.  
- Stop early if all characters in `s` are matched (avoid unnecessary work).  
- Make sure to handle cases where characters repeat in `t` but not in `s`.
