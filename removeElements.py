#   -*-   coding:   utf-8    -*-
'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
"""
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return head
        retHead = head
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        if retHead.val == val:
            return retHead.next
        return retHead

if __name__ == "__main__":
	sol = Solution()
