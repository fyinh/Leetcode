# coding=utf-8

"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# code
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1
        else:
            if (l1.val >= l2.val):
                tag = ListNode(l2.val)
                l2 = l2.next
            else:
                tag = ListNode(l1.val)
                l1 = l1.next
            result = tag
            while(l1 != None and l2 != None):
                if(l1.val >= l2.val):
                    tag.next = l2
                    tag = tag.next
                    l2 = l2.next
                else:
                    tag.next = l1
                    tag = tag.next
                    l1 = l1.next
            if(l1 == None):
                while(l2 != None):
                    tag.next = l2
                    tag = tag.next
                    l2 = l2.next
            else:
                while(l1 != None):
                    tag.next = l1
                    tag = tag.next
                    l1 = l1.next
            return result

