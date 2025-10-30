# Notes

## Link
https://leetcode.com/problems/binary-watch/

## Code
``` python
from collections import defaultdict

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:        
        def backtrack(i, cnt, _sum, _list, box, max_value):
            if _sum > max_value:
                return
            if i == len(_list) or cnt == turnedOn:
                box[cnt].add(_sum)
                return
            backtrack(i+1, cnt, _sum, _list, box, max_value)
            backtrack(i+1, cnt+1, _sum+_list[i], _list, box, max_value)

        H, M = [1,2,4,8], [1,2,4,8,16,32]
        h_box, m_box = defaultdict(set), defaultdict(set)
        backtrack(0, 0, 0, H, h_box, 11), backtrack(0, 0, 0, M, m_box, 59)

        answer = []
        for i in range(turnedOn+1):
            j = turnedOn - i
            for h in h_box[i]:
                for m in m_box[j]:
                    answer.append(f"{h}:"+f"{100+m}"[1::])
        return answer
```

## Idea
- Use backtracking to count all combinations of turned-on LEDs for hours and minutes.  
- Store possible sums in dictionaries `h_box` and `m_box` grouped by LED count.  
- Combine hours and minutes where total LEDs equal `turnedOn`.  
- Format minutes with `f"{100+m}"[1:]` to ensure two-digit formatting.

## Complexity
- **Time:** O(1) — constant range of hours/minutes.  
- **Space:** O(1) — limited combinations stored.

## Gotcha
- Prune when `_sum > max_value` (invalid hour/minute).  
- Use sets to prevent duplicates.  
- Hours ≤ 11, minutes ≤ 59.
