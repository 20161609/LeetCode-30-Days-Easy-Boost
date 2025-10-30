# Notes

## Link
https://leetcode.com/problems/majority-element/

## Code
``` python
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)        
        for v in nums:
            freq[v] += 1
            if freq[v] > n // 2:
                return v
```

## Idea
- Count the occurrences of each number using a frequency dictionary.  
- If any element’s count exceeds `n // 2`, return that element immediately.  
- This approach guarantees correctness since the problem assumes a majority element always exists.  
- Implements a simple counting version of the **Boyer–Moore Majority Vote** idea.

**Topic:** Boyer–Moore / Hash Counting

## Complexity
- **Time:** O(n) — iterate through all elements once.  
- **Space:** O(n) — dictionary stores up to all unique elements.

## Gotcha
- A true Boyer–Moore algorithm uses constant space by maintaining a candidate and count.  
- This implementation is easier to understand and still valid for the given constraints.  
- Ensure the array is not empty (LeetCode guarantees at least one element).
