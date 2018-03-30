#    -*-     coding: utf-8    -*-
'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
class Solution(object):
    def findElement(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = (low+high)/2
        while low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                mid = (low+high)/2
            else:
                low = mid + 1
                mid = (low+high)/2
        return -1
    def searchRange(self, nums, target):
        idx = self.findElement(nums, target)
        if idx == -1:
            return [-1,-1]
        iR, iL = idx+1 , idx-1
        while iL > -1 and nums[iL] == target:
            iL -= 1
        while iR < len(nums) and nums[iR] == target:
            iR += 1
        return [iL+1,iR-1]

if __name__ == "__main__":	
	sol = Solution()
	nums = [5]
	target = 5
	print(sol.searchRange(nums,target))
