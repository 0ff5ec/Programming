#   -*-    coding: utf-8    -*-
'''
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
'''
"""
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head
        backUp , h = head , head
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        k = k%len(nums)
        i = 0
        while i < k:
            nums.insert(0,nums.pop())
            i += 1
        i = 0
        while i < len(nums):
            backUp.val = nums[i]
            backUp = backUp.next
            i += 1
        backUp = None
        return h

if __name__ == "__main__":
	sol = Solution()
