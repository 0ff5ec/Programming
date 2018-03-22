# _*_ coding = utf-8 _*_
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
"""
        :type l1: ListNode
        :type l2: ListNode
	:type l: ListNode
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def genNumber(self, l):
        i = 1
        num = l.val
        while l.next != None:
            num += (l.next.val)*10**i
            l = l.next
            i += 1
        return num
    def addTwoNumbers(self, l1, l2):
        sol = Solution()
        ans = sol.genNumber(l1) + sol.genNumber(l2)
        l = ListNode(ans%10)
        backL = l
        ans = ans//10
        while ans != 0:
            backL.next = ListNode(ans%10)
            backL = backL.next
            ans = ans//10
        return l

if __name__ == "__main__":
	sol = Solution()
