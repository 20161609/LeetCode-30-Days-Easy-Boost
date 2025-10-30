# Notes

## Link
https://leetcode.com/problems/subsets/

## Code
``` python
from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer, stack = [], deque()
        def backtracking(i):
            if i == n:
                answer.append(list(stack))
                return
            backtracking(i+1)
            stack.append(nums[i])
            backtracking(i+1)
            stack.pop()

        backtracking(0)
        return answer
```

## Idea
- Use **backtracking** to generate all possible subsets of the input list `nums`.  
- For each element at index `i`, there are two choices:  
  1. **Exclude** the element → call `backtracking(i + 1)`  
  2. **Include** the element → append it to `stack`, call recursively, then pop.  
- When the index reaches `n`, append the current combination to `answer`.  
- This explores the full decision tree of inclusion/exclusion.

**Topic:** Backtracking

## Complexity
- **Time:** O(2ⁿ) — each element has two possible states (included/excluded).  
- **Space:** O(n) — recursion depth and temporary stack usage.

## Gotcha
- Always use `list(stack)` when appending to `answer` to avoid reference issues.  
- Make sure to pop after recursion to restore the previous state.  
- The order of subsets in the result doesn’t matter.
