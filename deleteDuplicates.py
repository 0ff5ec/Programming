'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
"""
        :type head: ListNode
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        ret_head = head
        while head != None and head.next != None:
            if head.val == (head.next).val:
                head.next = head.next.next
            if head.next != None and head.next.val != head.val:
                head = head.next
        return ret_head

if __name__ == "__main__":
	sol = Solution()
