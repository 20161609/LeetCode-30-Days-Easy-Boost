"""
Problem: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Topic: Linked List / Fast-Slow
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
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