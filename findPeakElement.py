#    -*-    coding: utf-8    -*-
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def findPeakElement(self, nums):
        if not len(nums):
            return -1
        if len(nums) == 1:
            return 0
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i += 1
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,4,5,6,7]
	print(sol.findPeakElement(nums))
