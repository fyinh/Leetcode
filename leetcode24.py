# coding=utf-8

"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# code
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head;head=p
        while p.next!=None and p.next.next!=None:
            s=p.next.next
            p.next.next=s.next
            s.next=p.next
            p.next=s
            p=s.next
        return head.next

