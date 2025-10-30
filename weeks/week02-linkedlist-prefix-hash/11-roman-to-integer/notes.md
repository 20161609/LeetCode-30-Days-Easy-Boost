# Notes

## Link
https://leetcode.com/problems/roman-to-integer/

## Code
``` python
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, '-': 0}
        answer, prev = 0, '-'
        for i in range(n-1):
            if rom[s[i]] >= rom[s[i+1]]:
                answer += rom[s[i]] - rom[prev]
                prev = '-'
            else:
                prev = s[i]
        answer += rom[s[-1]] - rom[prev]

        return answer
```

## Idea
- Convert a Roman numeral string into its integer value using a mapping dictionary.  
- Store symbol values in `rom`, including a placeholder `'-': 0` to simplify subtraction handling.  
- Iterate through the string from left to right:  
  - If the current symbol’s value is **greater or equal** to the next, add its value minus any pending previous symbol.  
  - Otherwise, mark the current symbol as `prev` for a potential subtraction (like `IV` or `IX`).  
- Finally, add the value of the last symbol minus any remaining `prev`.

**Topic:** String Parsing

## Complexity
- **Time:** O(n) — each Roman symbol is processed once.  
- **Space:** O(1) — fixed-size mapping dictionary.

## Gotcha
- Handles subtraction cases (e.g., `IV`, `IX`, `XL`, `XC`, `CD`, `CM`) using the `prev` marker.  
- The `'-'` key avoids boundary checks for the first character.  
- Must process the last symbol separately after the loop to ensure correct total.
