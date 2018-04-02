#    -*-    coding: utf-8    -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 2:
            return min(nums)
        low = 0
        high = len(nums) - 1
        mid = (low+high)//2
        while low < high:
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            mid = (low+high)//2
        return nums[low]

if __name__ == "__main__":
	sol = Solution()
	nums = [5,6,2,4]
	print(sol.findMin(nums))
