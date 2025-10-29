# Notes

## Code
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_reverse(left, right):
    if right.next:
        left = get_reverse(left, right.next)
    left.val, right.val = right.val, left.val
    return left.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        get_reverse(head, slow)
        return head
```

## Link
https://leetcode.com/problems/reverse-linked-list/

## Idea
- Recursively reverse the linked list by swapping values between the head (`left`) and the midpoint (`right`).
- Use a helper function `get_reverse(left, right)` to traverse to the end of the list, then swap node values during the unwind phase.
- Use slow/fast pointers to find the midpoint (`slow`) for symmetry in swapping.
- This approach **does not change node pointers**, only swaps node values.

**Topic:** Linked List / Recursion

## Complexity
- **Time:** O(n) — each node is visited once during recursion.
- **Space:** O(n) — due to recursion stack.

## Gotcha
- This solution reverses **node values**, not the actual node links.
- Works fine for palindrome-like value reversal, but not in-place pointer reversal.
- Be cautious with odd/even-length lists — midpoint (`slow`) ensures correct swap boundaries.
