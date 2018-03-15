'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def missingNumber(self, nums):
        l = len(nums)
        sum_total = (l*(l+1))//2
        sum_array = 0
        for i in nums:
            sum_array += i
        return sum_total - sum_array

if __name__ == "__main__":
	sol = Solution()
	nums = [0]
	print(sol.missingNumber(nums))
