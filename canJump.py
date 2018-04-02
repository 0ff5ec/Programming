#    -*-    coding: utf-8    -*-
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
"""
        :type nums: List[int]
        :rtype: bool
        """
class Solution(object):
    def canJump(self, nums):
        end = len(nums) - 1
        for i in range(end,-1,-1):
            if i + nums[i] >= end:
                end = i
        return end == 0

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,7,2,1,0,0,1,0,3]
	print(sol.canJump(nums))
