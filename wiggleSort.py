#    -*-    coding: utf-8    -*-
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''
"""
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        i = 1
        while i<len(nums)-1:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
            i += 2
        return

if __name__ == "__main__":
	sol = Solution()
	nums = [3,2,6,5,4,1]
	print(sol.wiggleSort(nums))
