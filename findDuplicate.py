#    -*-    coding: utf-8    -*-
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
1.You must not modify the array (assume the array is read only).
2.You must use only constant, O(1) extra space.
3.Your runtime complexity should be less than O(n2).
4.There is only one duplicate number in the array, but it could be repeated more than once.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def findDuplicate(self, nums):
        repeat = set()
        i = 0
        while i < len(nums):
            if nums[i] in repeat:
                return nums[i]
            repeat.add(nums[i])
            i += 1
        return -1

if __name__ == "__main__":
	sol = Solution()
	nums = [2,1,1,3,4]
	print(sol.findDuplicate(nums))
