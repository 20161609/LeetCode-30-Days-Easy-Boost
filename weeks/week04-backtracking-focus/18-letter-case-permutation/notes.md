# Notes

## Link
https://leetcode.com/problems/binary-watch/

## Code


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
