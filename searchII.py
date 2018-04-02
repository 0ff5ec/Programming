#    -*-    coding: utf-8    -*-
'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''
"""
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
class Solution(object):
    def search(self, nums, target):
        if(not nums):
            return False 
        low, high = 0, len(nums) - 1
        while(low < high):
            mid = (low + high)//2
            left, middle, right = nums[low], nums[mid], nums[high]
            if(middle == target):
                return True
            if(middle > right):
                if(left <= target < middle):
                    high = mid
                else:
                    low = mid + 1
            elif(middle < right):
                if(middle < target <= right):
                    low = mid + 1
                else:
                    high = mid
            else:
                high -= 1
        return nums[low] == target

if __name__ == "__main__":
	sol = Solution()
	nums = [3,4,5,6,0,1,2,3]
	target = 1
	print(sol.search(nums, target))
