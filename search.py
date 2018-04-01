#    -*-    coding: utf-8    -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
"""
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        
        while (low <= high):
            mid = (low+high)/2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return -1
    
    
        # O(n) time complexity linear search
        '''for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1'''

if __name__ == "__main__":	
	sol = Solution()
	nums , target = [9,10,3,5,6] , 6
	print(sol.search(nums, target))
