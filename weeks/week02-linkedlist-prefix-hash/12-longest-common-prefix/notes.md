# Notes

## Link
https://leetcode.com/problems/longest-common-prefix/

## Code
``` python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        box = []
        for i in range(min(len(s) for s in strs)):
            for s in strs:
                if strs[0][i] != s[i]:
                    return ''.join(box)
            box.append(strs[0][i])
        return ''.join(box)
```

## Idea
- Iterate character by character across all strings up to the length of the **shortest string**.  
- For each position `i`, compare the `i`-th character of every string with that of the first string.  
- If all characters match, append the character to `box`; otherwise, stop and return the prefix built so far.  
- Join all collected characters into a single prefix string at the end.

**Topic:** String

## Complexity
- **Time:** O(n × m) — where `n` is the number of strings and `m` is the length of the shortest string.  
- **Space:** O(m) — stores at most the length of the common prefix.

## Gotcha
- The list `strs` must not be empty (LeetCode guarantees at least one string).  
- Stops early on the first mismatch, avoiding unnecessary iterations.  
- Using `min(len(s) for s in strs)` ensures no index-out-of-range errors when comparing.