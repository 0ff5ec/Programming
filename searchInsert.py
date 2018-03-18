'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0
'''
"""
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
class Solution(object):
    def searchInsert(self, nums, target):
        l = len(nums)
        if l == 0:
            return 0
        low = 0
        high = len(nums)
        mid = (low + high)/2
        flag = 1
        while flag:
            if nums[mid] == target:
                return mid
            if low + 1 == high:
                return low if nums[low] >= target else high
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
            mid = (low+high)/2

if __name__ == "__main__":
	sol = Solution()
	nums, target = [-2,0,6,9], 8
	print(sol.searchInsert(nums,target))
