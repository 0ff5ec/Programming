#    -*-    coding: utf-8    -*-
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''
"""
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
class Solution(object):
    def sortColors(self, nums):
        l = len(nums)
        red = nums.count(0)
        blue = nums.count(2)
        white = nums.count(1)
        i = 0
        while i < red:
            nums[i] = 0
            i += 1
        while i < red + white:
            nums[i] = 1
            i += 1
        while i < l:
            nums[i] = 2
            i += 1
        return 

if __name__ == "__main__":
	sol = Solution()
	nums = [1,1,1,2,0,0,1,2,1]
	print(sol.sortColors(nums))
