# -*- coding: utf-8 -*-

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def majorityElement(self, nums):
        nums = sorted(nums)
        cnt = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                cnt += 1
                if cnt > len(nums)/2:
                    return nums[i]
            else:
                cnt = 1

if __name__ == "__main__":
	sol = Solution()
	nums = [1]
	print(sol.majorityElement(nums))
