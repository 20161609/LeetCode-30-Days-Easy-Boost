# Notes

## Link
https://leetcode.com/problems/valid-palindrome/

## Code
``` python
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        box = deque()
        for c in s:
            if c.isalpha() or c.isnumeric():
                box.append(c.lower())
        s = ''.join(box)
        return s==s[::-1]
```

## Idea
- Filter out only **alphanumeric** characters and convert everything to lowercase.  
- Use **two-pointer** or **string reversal** comparison to check if it reads the same forward and backward.  
- Can use `deque` for efficient popping or just simple string slicing in Python.  
- Ignore spaces, punctuation, and capitalization entirely.

**Topic:** Two Pointers

## Complexity
- **Time:** O(n) — need to traverse the entire string once  
- **Space:** O(n) — for storing filtered characters (can be reduced to O(1) with two-pointer approach directly on string)

## Gotcha
- Must ignore **non-alphanumeric** characters (e.g., `"A man, a plan, a canal: Panama"`).  
- Don’t forget to lowercase before comparing.  
- Avoid using `isalnum()` incorrectly — it already covers both `isalpha()` and `isdigit()`.