#    -*-    coding: utf-8     -*-
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        reference = nums[-1]
        while low + 1 < high:
        	mid= (low+high)//2
        	if nums[mid] > reference:
        		low = mid
        	elif nums[mid] < reference:
        		high = mid	
        	elif nums[mid] == reference:
        		if nums[low] < reference:
        			high -= 1
        		else:
        			low += 1 
        return nums[low] if nums[low] < reference else nums[high]

if __name__ == "__main__":
	sol = Solution()
	nums = [3,1,3]
	print(sol.findMin(nums))
