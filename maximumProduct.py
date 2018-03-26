#   -*-    coding: utf-8    -*_
'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        nums = sorted(nums)
        if nums[1] < 0:
            return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        else:
            return nums[-1]*nums[-2]*nums[-3]

if __name__ == "__main__":
	sol = Solution()
	nums = [1,2,-100,5,-2,0]
	print(sol.maximumProduct(nums))
