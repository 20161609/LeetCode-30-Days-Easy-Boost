# Notes

## Link
https://leetcode.com/problems/assign-cookies/

## Code
``` python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()        
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i+= 1
            j += 1

        return i
```

## Idea
- Use a **greedy** approach to maximize the number of content children.  
- Sort both greed factors `g` and cookie sizes `s`.  
- Assign the smallest cookie that can satisfy each child.  
- Move to the next child only when the current one is satisfied.

**Topic:** Greedy

## Complexity
- **Time:** O(n log n) — sorting dominates.  
- **Space:** O(1)

## Gotcha
- Always increment cookie index `j`, but only increment child index `i` when satisfied.  
- Sorting ensures minimal cookie usage for each child.
