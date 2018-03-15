# -*- coding: utf-8 -*-
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num =5  you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
"""
        :type num: int
        :rtype: List[int]
        """
class Solution(object):
    def countBits(self, num):
        a0 = [0]
        a1 = [1]
        ans = a0 + a1
        n = num
        prev = a1
        while n != 0:
            if n//2 != 0:
                new = prev + [(i+1) for i in prev]
                ans = ans + new
                prev = new
            n = n//2
        return ans[:num+1]

if __name__ == "__main__":
	sol = Solution()
	print(sol.countBits(int(raw_input("Enter the number: "))))
