#   -*- coding: utf-8   -*-
'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        '''i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
	print(nums[:i+1])
        return i+1'''
        i = 1
        count = 0
        while i < len(nums) - count:
            if nums[i] == nums[i-1]:
                nums = nums[:i]+nums[i+1:]+[nums[i]]
                count += 1
            else:
                i += 1
	print(nums[:len(nums) - count])
        return len(nums) - count

if __name__ == "__main__":
	sol = Solution()
	nums = [1,1,3]
	print(sol.removeDuplicates(nums))
