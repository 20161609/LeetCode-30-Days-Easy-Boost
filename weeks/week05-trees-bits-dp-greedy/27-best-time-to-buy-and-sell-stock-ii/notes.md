# Notes

## Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## Code
``` python
from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, stack = 0, deque()
        for p in prices:
            if stack and stack[-1] > p:
                answer += stack[-1] - stack[0]
                stack.clear()
            stack.append(p)
        if stack:
            answer += stack[-1] - stack[0]
        return answer
```

## Idea
- Use a **greedy** approach: accumulate profit every time the price goes up.  
- Buy before each rise and sell at each local peak.  
- Simply sum up all positive differences between consecutive prices.

**Topic:** Greedy

## Complexity
- **Time:** O(n) — single pass through prices.  
- **Space:** O(1)

## Gotcha
- Skip consecutive equal prices (no gain).  
- Works even with multiple buy/sell cycles.  
- Final profit equals the total of all upward movements.
