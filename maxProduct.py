#    -*-    coding: utf-8    -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
"""
        :type nums: List[int]
        :rtype: int
        """
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = currMax
                currMax = currMin
                currMin = tmp
            currMax = max(nums[i], currMax*nums[i])
            currMin = min(nums[i], currMin*nums[i])
            maxProd = max(maxProd, currMax)
        return maxProd

if __name__ == "__main__":
	sol = Solution()
	nums = [-1,-3,0,-4]
	print(sol.maxProduct(nums))
