# Notes

## Link
https://leetcode.com/problems/linked-list-cycle/

## Code
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            if slow != head and slow == fast or slow == fast.next:
                return True
            slow, fast = slow.next, fast.next.next
        return False
```

## Idea
- Use **two pointers (slow & fast)** to detect a cycle in a linked list.  
- Move `slow` one step and `fast` two steps at a time.  
- If they ever point to the same node, a cycle exists.  
- If `fast` or `fast.next` becomes `None`, the list terminates and has no cycle.  
- This implementation compares both `slow == fast` and `slow == fast.next` as an additional safeguard.

**Topic:** Linked List / Fast-Slow (Floyd’s Cycle Detection)

## Complexity
- **Time:** O(n) — each pointer moves at most `n` steps.  
- **Space:** O(1) — only uses two pointers.

## Gotcha
- Must check both `fast` and `fast.next` in the loop condition to avoid `NoneType` errors.  
- The condition `slow == fast.next` can sometimes trigger earlier detection, but standard Floyd’s algorithm uses only `slow == fast`.  
- Ensure you return `False` when the loop exits naturally (no meeting point → no cycle).
