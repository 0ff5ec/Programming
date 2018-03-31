#    -*-    coding: utf-8    -*-
'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
"""
        :type nums: List[int]
        :rtype: List[int]
        """

class Solution(object):
    def productExceptSelf(self, nums):
        output = [None]*len(nums)
        output[0] = 1
        for i in range(1,len(nums)):
            output[i] = output[i-1]*nums[i-1]
        trailing = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            output[i] = output[i]*trailing
            trailing *= nums[i]
        return output

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,4,5,3,6,8,0]
	print(sol.productExceptSelf(nums))
