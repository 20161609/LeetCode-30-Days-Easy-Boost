"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Topic: Linked List
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
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