# -*- coding: utf-8 -*-
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def singleNumber(self, nums):
        ret = 0
        for a in nums:
            ret = ret^a
        return ret

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,2,3,3,4,4,5,5]
	print(sol.singleNumber(nums))
