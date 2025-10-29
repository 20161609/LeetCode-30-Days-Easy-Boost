# Notes

## Link
https://leetcode.com/problems/merge-two-sorted-lists/

## Code
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 enter list2
        if list1 == None:
            return list2
        if list2 == None:
            return list1        
        if list1.val < list2.val:
            list1, list2 = list2, list1
        node1, node2 = list1, list2

        while node1 and node2 and node2.next:
            if node1.val < node2.next.val:
                tmp1 = node1.next
                node1.next, node2.next = node2.next, node1
                node1 = tmp1
            else:
                node2 = node2.next
            
        if node1:
            node2.next = node1
        return list2
```

## Idea
- Given two **sorted linked lists**, merge them into a single sorted list.  
- Use a **dummy head** pointer to simplify merging, or handle one list node-by-node.  
- Always attach the node with the smaller value to the merged list, then move that list’s pointer forward.  
- Continue until one of the lists is exhausted, then attach the remaining nodes.

**Topic:** Linked List / Two Pointers

## Complexity
- **Time:** O(n) — each list is traversed once.  
- **Space:** O(1) — merging is done in place (no extra list allocated).

## Gotcha
- Always check for `None` before accessing `.val` or `.next`.  
- Avoid reversing order — both lists are already sorted ascendingly.  
- Edge cases: one list empty, both lists empty, or identical values.