#   -*-   coding:   utf-8   -*-
'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
"""
        :type nums: List[int]
        :rtype: bool
        """
class Solution(object):
    def containsDuplicate(self, nums):
        return False if len(set(nums)) == len(nums) else True

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,3,4,5,6,3]
	print(sol.containsDuplicate(nums))
